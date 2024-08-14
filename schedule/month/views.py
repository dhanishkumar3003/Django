from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

Month = {
    "jan": "Learning Python",
    "feb": "Sleeping",
    "mar": None,
    "april": "April Fool"
}

def index(request):
    months = list(Month.keys())
    return render(request, 'month/index.html', {'months': months} )


def month_in_number(request, month):
    months = list(Month.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Data Not Found</h1>")
    month_name = months[month - 1]
    redirect_path = reverse("month-detail", args=[month_name])
    return HttpResponseRedirect(redirect_path)

def month_details(request, month):
    if month in Month:
        month_text = Month[month]
        return render(request, "month/month.html", {"text": month_text})
    else:
        return HttpResponseNotFound(f"<h1>{month} Not Found</h1>")
