from django.shortcuts import render,redirect
from django.http import HttpResponse
from cont.models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return  render(request,'about.html')

def contact(request):
     if request.method =='POST':
           name=request.POST.get('name')
           email=request.POST.get('email')
           phone=request.POST.get('phone')
           contact=Contact(name=name, email=email, phone=phone)
           contact.save()
           messages.success(request, 'Contact has been sent.')
        #    return redirect(request,'index.html')
     return render(request,'contact.html')
