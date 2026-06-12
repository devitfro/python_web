from django.urls import path
from . import views

urlpatterns = [
    # главная
    path('', views.home, name='home'),

    # фильмы
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='movie_create'),
    path('movie/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),

    # отзывы
    path(
        'movie/<int:movie_pk>/review/<int:review_pk>/delete/',
        views.review_delete,
        name='review_delete'
    ),

    # auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]