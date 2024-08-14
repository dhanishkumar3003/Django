from django.urls import path
from .views import index, month_in_number, month_details

urlpatterns = [
    path("<int:month>", month_in_number),
    path("<str:month>", month_details, name="month-detail"),
    path("index/", index)
]
