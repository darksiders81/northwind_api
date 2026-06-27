"""
URL configuration for core project.

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
from django.urls import include, path

from .ApiDoc import apiDocUrlpatterns



urlpatterns = [
    path('api/' , include('Categories.urls')),
    path('api/' , include('Customer.urls')),
    path('api/' , include('Employees.urls')),
    path('api/' , include('Territories.urls')),
    path('api/' , include('Shippers.urls')),
    path('api/' , include('Products.urls')),
    path('api/' , include('Orders.urls')),
    path('api/' , include('Suppliers.urls')),
    path('api/' , include('UsStates.urls')),
    
    
    
    # path('admin/', admin.site.urls),
] + apiDocUrlpatterns
