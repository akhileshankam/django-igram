from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.contrib import messages

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return redirect('signup')
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        if(username and password and cpassword and email):
            if cpassword==password:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()

                return render(request,'confirmation.html')
            else:
                return HttpResponse('passwords didnt match')
        else:
            return HttpResponse("enter all fields")





# Create your views here.
