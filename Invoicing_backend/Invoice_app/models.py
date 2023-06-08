from django.db import models

# Create your models here.
from django.db import models


        
        
class User(models.Model):
    user_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
class Invoices(models.Model):
        invoice_id=models.IntegerField()
        client_name=models.CharField(max_length=200)
        date=models.DateField()


class Items(models.Model):
    invoice=models.ForeignKey(Invoices,on_delete=models.CASCADE,blank=True,null=True,related_name="item_list") 
    desc=models.TextField(max_length=200)
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()


        
