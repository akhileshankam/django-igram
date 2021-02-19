from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('login1/',views.login1,name='login1'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('likeb/',views.likeb,name='likeb'),
    path('comments/',views.comments,name='comments'),
    path('chatform/',views.chatform,name='chatform'),
    path('chatresponse/',views.chatresponse,name='chatresponse'),
    path('inbox/',views.inbox,name='inbox'),





]

