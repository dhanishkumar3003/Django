from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', AuthorList),
    path("<int:authid>", AuthorInfo,name="AuthorInfoUsingId"),
    path("<str:authslug>", AuthorInfoSlug,name="AuthorInfoUsingSlug"),
]