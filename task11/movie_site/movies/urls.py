from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]