
from django.urls import path,include
from .import views

urlpatterns = [
    path('<int:week>', views.week_num),
    path('<str:week>', views.week_string,name='month-detail'),
]
