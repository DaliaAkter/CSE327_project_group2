"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('view_mynotes',view_mynotes,name='view_mynotes'),
path('delete_mynotes/<int:pid>', delete_mynotes,name='delete_mynotes'),
path('view_users',view_users,name='view_users')
path('delete_users/<int:pid>', delete_users,name='delete_users'),
]+static(settings.Media_URL,document_root=settings.MEDIA_ROOT)
