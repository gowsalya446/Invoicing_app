from django.urls import path
from .views  import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('invoices', csrf_exempt(AllInvoice.as_view()),name="all_invoices"),
    path('invoices/new', csrf_exempt(AllInvoice.as_view()),name="newinvoices"),
    path('invoices/<int:id>',csrf_exempt(Single_invoice.as_view()),name="Invoice_id"),
    path('invoices/<int:invoice_id>/items',csrf_exempt(Single_invoice.as_view()),name="update_item"),
    path('user/signup',csrf_exempt(Signup.as_view()),name="sign_up"),
    path('user/login',csrf_exempt(SignIn.as_view()),name="sign_in")

    
]