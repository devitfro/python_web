from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_tasks, name='daily_tasks'),
]