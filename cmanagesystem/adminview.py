from django.core.checks import messages
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Q
from cmanagesystem.models import Agent, Customer, Product, ProductName, actionTable, call, listTest, productType
from datetime import datetime

def adminPanel(request):
    return render(request, "adminpanel.html")

# Add Products

def addProductPage(request):
    prodName = ProductName.objects.all()
    itemtype = productType.objects.all()
    cust = Customer.objects.all()
    return render(request, 'addproduct.html', {"prodN":prodName, "itemT":itemtype, "customer":cust})

def productAdd(request):
    if request.method == "POST":
        srno = request.POST["serialNo"]
        prname = request.POST.get("pname")
        product = ProductName.objects.get(id=prname)
        itmtype = request.POST["itrm"]
        item = productType.objects.get(id=itmtype)
        cname = request.POST["cname"]
        ccontact = request.POST["ccont"]
        addr = request.POST["address"]
        reg = request.POST["region"]

        newproduct = Product.objects.create(serialNumber=srno, Name=product, itemType=item, customerName=cname, Address=addr,
                     custContact=ccontact, Region=reg)
        return HttpResponse("success")

def addAgent(request):
    return render(request, "addagent.html")

def newAgent(request):
    if request.method == "POST":
        agentname = request.POST["aname"]
        ausername = request.POST["auname"]
        apassword = request.POST["apass"]

        newagent = Agent.objects.create(agentName=agentname, username=ausername, password=apassword)
        # return render(request, "adminpanel.html")
        return redirect(adminPanel)