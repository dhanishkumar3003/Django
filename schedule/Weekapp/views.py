from django.shortcuts import render
from django.http import *
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

dates = {
    "Monday":"very booring",
    "thursday":"booring",
    "wednesday":"Not bad",
    "Tuesday":"Good",
    "Friday":"very Good",
    "Saturday":"Very Happy",
    "Sunday":"Very Very Happy",
}

def days_in_number(request,days):
    dates_lists = list(dates.keys())
    try:
        if days>len(dates_lists):
            return HttpResponseNotFound(f"<h1>Not Found<h1>")
    except:
        day = dates_lists[days-1]
        redirect_days = render_to_string("month/month.html")
        return HttpResponseRedirect(redirect_days)

def days_in_string(request,days):
    try:
        days = dates[days]
        return HttpResponse(f"<h1>{days}<h1>")
    except:
        return HttpResponseNotFound(f"<h1>Not Found<h1>")
    
    