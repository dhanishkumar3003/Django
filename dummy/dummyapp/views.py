# dummyapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("It works")
def dhanish(request):
    return HttpResponse("I'm Dark Prince")