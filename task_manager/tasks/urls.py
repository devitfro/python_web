from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list),
    path('add/', views.add_task),
    path('delete/<int:id>/', views.delete_task),
]