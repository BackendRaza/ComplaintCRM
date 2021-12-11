from django.urls import path, include
from . import views, adminview

urlpatterns = [
    path("home/", views.home, name="Home"),
    path("", views.login, name="Login"),
    path("agentLogin/", views.agentLogin, name="AgentLogin"),
    path("logout/", views.logout, name="logout"),
    path("creatcall/", views.newCall, name="newCall"),
    path("search/", views.searchCall, name="Search"),
    path("addproductpage/", adminview.addProductPage, name="addProductPage"),
    path("addCall/", views.addCall, name="addCall"),
    path("editcall/<int:pk>", views.editCall, name="editCall"),
    path("updatecall/<int:pk>", views.updateCall, name="updateCall"),
    path("calldetails/<int:pk>", views.searchByProd, name="searchByProd"),
    path("productadd/", adminview.productAdd, name="productAdd"),
    path("addagent/", adminview.addAgent, name="addAgent"),
    path("newagent/", adminview.newAgent, name="newAgent"),
    path("adminpanel/", adminview.adminPanel, name="AdminPanel")

]