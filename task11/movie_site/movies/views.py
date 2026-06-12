from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Movie, Review
from .forms import MovieForm, ReviewForm

# главная страница
def home(request):
    return render(request, 'base.html')


# список фильмов
def movie_list(request):
    sort_by = request.GET.get('sort', 'release_date')
    movies = Movie.objects.all().order_by(sort_by)

    return render(request, 'movies/movie_list.html', {
        'movies': movies
    })


# детальная страница + отзывы
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.username = request.user.username  # теперь реальные юзеры
            review.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })


# добавить фильм
@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'movies/movie_form.html', {'form': form})


# редактировать фильм
@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {'form': form})


# удалить фильм
@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})


# удалить отзыв
@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk, movie_id=movie_pk)

    if request.method == 'POST':
        review.delete()
        return redirect('movie_detail', pk=movie_pk)

    return render(request, 'movies/review_confirm_delete.html', {
        'review': review
    })


# регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})


# логин
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie_list')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

# logout
def logout_view(request):
    logout(request)
    return redirect('home')