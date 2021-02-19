from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, comment, messages


def home(request):
    if request.user.is_authenticated:
        data = Post.objects.all().order_by('title')
        data2 = comment.objects.all().order_by('title')
        return  render(request,'home2.html',{'data':data,'data2':data2})
    else:
        data = Post.objects.all().order_by('title')
        return render(request, 'home.html', {'data': data})
# Create your views here.


def login1(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if(username and password):
            user=authenticate(username=username,password=password)
            data = Post.objects.all()
            data2 = comment.objects.all()
            if user is not None:
                auth.login(request,user)
                return render(request,'home2.html',{'data':data,'data2':data2})
            else:
                return HttpResponse("login failed")
        else:
            return HttpResponse("enter all fields")


def login(request):
    data = Post.objects.all().order_by('title')
    data2=comment.objects.all()
    if request.method == "POST":
        title= request.POST['title']
        image = request.FILES.get('image')
        username=request.user.username

        if title and image:
            x = Post(title=title, image=image,username=username)
            x.save()
            return render(request, 'home2.html',{'data':data,'data2':data2})
        else:
            return HttpResponse("FAILED")
def myprofile(request):
    data = Post.objects.filter(username=request.user.username)
    return render(request,'myprofile.html',{'data':data})


from django.shortcuts import render
def likeb(request):
    post_title=request.POST['post_title']
    data=Post.objects.filter(title=post_title)
    for i in data:
        i.likes2.add(request.user)
        data = Post.objects.all().order_by('title')
        return render(request, 'home2.html', {'data': data})
def comments(request):
    if request.method=="POST":
        com=request.POST['com']
        ptitle=request.POST['ptitle']
        username=request.POST['username']
        x=comment(text=com,title=ptitle,username=username)
        x.save()
        return redirect('/')

def chatform(request):
    data=User.objects.all().exclude(username=request.user.username)
    data2 = messages.objects.all()
    return render(request,'chat.html',{'data':data,'data2':data2})
def chatresponse(request):
    fromusername=request.POST['fromusername']
    mssg=request.POST['text']
    tousername = request.POST['tousername']
    x=messages(fromusername=fromusername,mssg=mssg,tousername=tousername)
    x.save()
    return redirect('chatform')
def inbox(request):
    data=messages.objects.all()
    return render(request,'chatform2.html',{'data':data})





# Create your views here.
