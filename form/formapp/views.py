from django.shortcuts import render, redirect, HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name','')
        l_name = request.POST.get('l_name','')
        phone_number = request.POST.get('phone_number','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        password = request.POST.get('password','')
        if f_name and l_name and email and address and phone_number and password:
            contact = Contact(f_name=f_name,l_name=l_name,email=email,address=address,password=password,phone_number=phone_number)
            contact.save()
        else:
            HttpResponse("Please fill up the form correctly")

    return render(request,'index.html')