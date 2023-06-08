from rest_framework import serializers
from .models import User,Invoices,Items


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

        
class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields=['desc','rate','quantity']  
        
class Invoiceserializer(serializers.ModelSerializer):
    items=Itemserializer(many=True)
    class Meta:
        model=Invoices
        fields="__all__"                
              