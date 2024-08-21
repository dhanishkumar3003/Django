
from django.urls import path,include
from .import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('dhanish',views.dhanish),

    path('<int:month>', views.monthly_details_num),
    path('<str:month>', views.monthly_details,name='month-detail'),
]
