
from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('userinfoform/', views.UserInfoForm),
]
from django.urls import path
from . import views
urlpatterns = [
    path('',views.feedbackform),
    path('thankyou',views.thanku)
 
]