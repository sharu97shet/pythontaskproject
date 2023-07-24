"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views



urlpatterns = [
    path('',views.task,name='task'),
    path('login',views.login,name='login'),
    path('addtask',views.addtask,name='addtask'),
    path('insertblog',views.ContactView,name='insertblog'), 
    path('addblog',views.addblog,name='addblog'), 
    path('tasklist',views.tasklist,name='tasklist'),
    path('profile',views.profile,name='tasklist'),

    path('accounts/', include('allauth.urls')),

    path('loginusername/<str:email>',views.loginusername,name='tasklist'),
    path('useraccount',views.useraccount,name='useraccount'),

    path('register',views.register,name='register'),
    path('forgot_password',views.forgot_password,name='register'),
    path('userregister',views.userregister,name='userregister'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),

    #path('admin/', admin.site.urls),
]
