# coding: utf-8

from django.urls import path
from rest_framework import routers
from .views import*

"""
urlpatterns = [
    path('users/', UserViewSet),
]
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)