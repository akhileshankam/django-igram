from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
def signup(request):
    return render(request,'register.html')