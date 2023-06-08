from django.shortcuts import render
from django.views import View
from django.http import JsonResponse,Http404,HttpResponseBadRequest
from .serializer import Userserializer,Invoiceserializer,Itemserializer
from .data import *
import json
import uuid


class AllInvoice(View):
    def get(self,request):
        serializer=Invoiceserializer(invoicedata,many=True).data
        return JsonResponse(serializer,safe=False)
    
    def post(self,request):
        data=json.loads(request.body)
        data["invoice_id"]=len(invoicedata)+1
        print(data)
        serializer=Invoiceserializer(data=data)
        if serializer.is_valid():
            invoicedata.append(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
    
class Single_invoice(View):   
    
    def get(self,request,id):
        invoicefound=None
        for item in invoicedata:
            if item["invoice_id"]==id:
                invoicefound=item
                break
        if invoicefound:
              return JsonResponse(Invoiceserializer(invoicefound).data,safe=False)
        else:
              raise Http404("invoice Not found")  
 

    def post(self,request,invoice_id): 
        data=json.loads(request.body)
        serializer=Itemserializer(data=data)
        if serializer.is_valid():
            for item in invoicedata:
               if item["invoice_id"]==invoice_id:
                  invoicefound=item
                  break
            if invoicefound:
                item["items"].append(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        else:
            raise Http404("invoice Not found")  
        
class Signup(View):
    def post(self,request):
      user_data=json.loads(request.body)
      user_data['user_id']=len(userdata)+1
      user_serialized=Userserializer(data=user_data)


      if(user_serialized.is_valid()):
         userdata.append(Userserializer.data)

         return JsonResponse("Successfully registration done",safe=False,status=201)

      else:
         return HttpResponseBadRequest() 
class SignIn(View):     
    def post(self,request):
        data=json.loads(request.body)
        for index,item in enumerate(userdata):
            if(item["email"]==data["email"])and (item["password"]==data["password"]):
                token=str(uuid.uuid1())
                return JsonResponse({'message':"Successfully Login done","token":token,"state":True},safe=False)
            else:
                 return JsonResponse("login details is wrong")
         
            
             

                

        
        




# Create your views here.
