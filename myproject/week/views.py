from django.shortcuts import render
from django.http import *

# Create your views here.
def week_num(request,week):
    if week==1:
        return HttpResponseRedirect('/week/mon')
    elif week==2:
        return HttpResponseRedirect('/week/tue')
    elif week==3:
        return HttpResponseRedirect('/week/wed')
    elif week==4:
        return HttpResponseRedirect('/week/thu')
    elif week==5:
        return HttpResponseRedirect('/week/fri')
    elif week==6:
        return HttpResponseRedirect('/week/sat')
    elif week==7:
        return HttpResponseRedirect('/week/sun')
    else:
        return HttpResponse("Invalid week")
def week_string(request,week):
    if week=="mon":
        return HttpResponse("It's Monday")
    elif week=="tue":
        return HttpResponse("It's Tuesday")
    elif week=="wed":
        return HttpResponse("It's Wednesday")
    elif week=="thu":
        return HttpResponse("It's Thursday")
    elif week=="fri":
        return HttpResponse("It's Friday")
    elif week=="sat":
        return HttpResponse("It's Saturday")
    elif week=="sun":
        return HttpResponse("It's Sunday")
    else:
        return HttpResponse("Invalid week")