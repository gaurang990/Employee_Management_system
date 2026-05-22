"""
URL configuration for Employee_Records_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',home,name='home'),
     path('admin_home',admin_home,name='admin_home'),
     path('login',user_login,name='login'),
     path('add_employee',add_employee,name='add_employee'),
     path('Logout',Logout,name='logout'),
     path('employee_home',employee_home,name='employee_home'),
     path('apply_leave/', apply_leave, name='apply_leave'),
     path('leave_emp/', leave_emp, name='leave_emp')
]
