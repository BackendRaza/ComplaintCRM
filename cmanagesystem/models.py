import re
from typing import Match
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import RelatedField

class Customer(models.Model):
    Name = models.CharField(max_length=150)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=150)
    Region = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.Name

class productType(models.Model):
    type = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.type

class ProductName(models.Model):
    prodName = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.prodName

class Product(models.Model):
    serialNumber = models.CharField(max_length=150)
    Name = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    itemType = models.ForeignKey(productType, on_delete=models.CASCADE)
    customerName = models.CharField(max_length=150)
    Address = models.TextField()
    custContact = models.CharField(max_length=20)
    Region = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.serialNumber

class Agent(models.Model):
    agentName = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.agentName

class actionTable(models.Model):
    actionDetail = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.actionDetail

class approvalTable(models.Model):
    approvalDetail = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.approvalDetail

class call(models.Model):
    agent = models.CharField(max_length=20)
    callNature = models.ForeignKey(productType, on_delete=models.CASCADE)
    srNumber = models.ForeignKey(Product, on_delete=models.CASCADE)
    cContact = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cont")
    remark = models.TextField()
    action = models.TextField()
    approval = models.TextField(blank=True)
    time = models.DateTimeField()

    def __str__(self) -> str:
        return self.remark


class listTest(models.Model):
    name = models.CharField(max_length=150)
    hobbies = models.TextField()

    def set_list(self, element):
        if self.hobbies:
            self.hobbies = self.hobbies + "," + element

    def get_list(self):
        if self.hobbies:
            return self.hobbies.split(",")
        return None

