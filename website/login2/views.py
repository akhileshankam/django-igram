from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
# Create your views here.
def login2(request):
    return render(request,'login.html')