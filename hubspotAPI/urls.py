from django.contrib import admin
from django.urls import path
from .views.auth_view import *
from .views.api_view import ContactViews

urlpatterns = [
    path('', index, name='index'),
    path('auth/', auth, name='auth'),
    path('logoff/', logoff, name='logoff'),
    path('api/', ContactViews.as_view())
]