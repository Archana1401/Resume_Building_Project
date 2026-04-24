"""
URL configuration for resume_project project.

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
from resume_app import views

urlpatterns = [
    path('', views.resume_list, name='list'),
path('create/', views.create_resume, name='create'),
path('view/<int:id>/', views.view_resume, name='view'),
path('edit/<int:id>/', views.edit_resume, name='edit'),
path('delete/<int:id>/', views.delete_resume, name='delete'),
path('download/<int:id>/', views.download_pdf, name='download'),
]
