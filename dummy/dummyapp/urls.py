# dummyapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),  # Added a trailing slash for consistency
]
