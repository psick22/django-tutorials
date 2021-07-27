from django.contrib import admin
from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path('first', views.first),
    path('inside', Another.as_view())
]
