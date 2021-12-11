from django.core.checks import messages
from django.db.models.manager import EmptyManager
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Q
from cmanagesystem.models import Agent, Customer, Product, ProductName, actionTable, approvalTable, call, listTest, productType
from datetime import datetime
from django.contrib import messages

def home(request):
    agent = request.session["agentName"]
    calls = call.objects.all().filter(agent=agent)
    print(agent)
    return render(request, 'index.html', {'call': calls})

def login(request):
    return render(request, 'login.html')

def agentLogin(request):
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['upass']
        agent = Agent.objects.get(username=uname)
        if agent:
            if agent.password == upass:
                request.session['Id'] = agent.id
                request.session['agentName'] = agent.agentName
                request.session['username'] = agent.username
                return redirect(home)
            else:
                message = "Password is incorrect"
                return render(request, "login.html", {'msg': message})
        else:
            message = "This UserName does not exist!! Please Register"
            return render(request, "login.html", {'msg': message})


def logout(request):
    request.session.clear()
    message = "User Logged out!!!!!!"
    return redirect(login)

# Calls

def newCall(request):
    protype = productType.objects.all()
    prod = Product.objects.all()
    calls = actionTable.objects.all()
    actions = actionTable.objects.all()
    approvals = approvalTable.objects.all()
    # ptype = Product.objects.get(itemType=prod)
    return render(request, 'createcall.html', {"pro":protype,"protype":prod, "calls":calls, "act":actions, "appr":approvals})

def editCall(request, pk):
    protype = productType.objects.all()
    prod = Product.objects.all()
    cal = call.objects.get(id=pk)
    actions = actionTable.objects.all()
    approvals = approvalTable.objects.all()
    return render(request, "updatecall.html", {"key": cal, "pro":protype,"protype":prod, "act":actions, "appr":approvals})

def updateCall(request, pk):
    cdata = call.objects.get(id=pk)
    cnatur = request.POST.get("cnature")
    cn = productType.objects.get(id=cnatur)
    cdata.callNature = cn
    srn_number = request.POST.get("srnumber")
    srn = Product.objects.get(id=srn_number)
    cdata.srNumber = srn
    ccontact = request.POST.get("ccont")
    cc = Product.objects.get(id=ccontact)
    cdata.cContact = cc
    cdata.remark = request.POST["remark"]
    action = request.POST['action1']
    action=action.replace('\n','')
    action=action.replace('\u00D7','')
    action=action.replace(' ,',',')    
    cdata.action=action.strip()    
    approval = request.POST["approval"]
    cdata.approval=approval
    cdata.time = datetime.now()
    cdata.save()
    return redirect(home)


def addCall(request):
    if request.method == "POST":
        aid = request.POST.get("agentid")
        agentid = Agent.objects.get(id=aid)
        cnatur = request.POST.get("cnature")
        cn = productType.objects.get(id=cnatur)
        srn_number = request.POST.get("srnumber")
        srn = Product.objects.get(id=srn_number)
        ccontact = request.POST.get("ccont")
        cc = Product.objects.get(id=ccontact)
        remark = request.POST["remark"]
        Action = request.POST.get("action1")
        time = datetime.now()
        approve = request.POST.get("approval")      
        newcall = call.objects.create(agent=agentid, callNature=cn, srNumber=srn, cContact=cc, remark=remark, 
                                        action=Action, approval=approve, time=time)
    return redirect(home)


def searchCall(request):
    if request.method == "POST":
        searched_sr = request.POST["serial_sr"]        
        lookup = (Q(serialNumber=searched_sr) | Q(custContact=searched_sr))
        productsr = Product.objects.filter(lookup)
        return render(request, "createcall.html", {"productsr": productsr})
    else:
        return HttpResponse("Bad Request")

def searchByProd(request, pk):
    # calldetails = call.objects.all()
    prod = Product.objects.get(id=pk)
    cal = call.objects.filter(srNumber=prod)
    return render(request, "createcall.html", {"cals":cal})

