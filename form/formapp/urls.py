from django.urls import path, include
from formapp import views

urlpatterns = [
    path('', views.index,name='index'),
]
