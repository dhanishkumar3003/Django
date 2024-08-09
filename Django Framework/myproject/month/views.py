from django.shortcuts import render
from django.http import *
# Create your views here.

month_schedule = {
    'jan' : 'Learning Python',
    'feb' : 'Learning Java',
    'mar' : 'Happy birthday to Me',
    'aprl' : 'Learning React',
    'may' : 'learnign .net'
}

def monthly_details_num(request,month):
    months = list(month_schedule.keys())
    if month>11:
        return HttpResponse("Invalid month")
    if (month > len(months)):
        return HttpResponseNotFound('Request is Not Found')
    else:
        month_key = months[month]
    # month_text = month_schedule[month_key]
        return HttpResponseRedirect('/month/'+month_key)


def monthly_details(request,month):
    try:
        month_text = month_schedule[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound('This is not Mentioned')

def index(request):
    return HttpResponse("This Works!")

def dhanish(request):
    return HttpResponse("My name is dhanish")