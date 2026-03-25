from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    country = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='posters/')
    rating = models.PositiveSmallIntegerField(default=1)
    genre = models.ManyToManyField(Genre, blank=True, related_name='movies')  # изменено на ManyToMany

    class Meta:
        permissions = [
            ("can_change_movies", "Can change movies"),  # только суперпользователи
        ]

    def __str__(self):
        return self.title

    def reviews_count(self):
        return self.reviews.count()
    reviews_count.short_description = 'Количество отзывов'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=50, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ("can_moderate_reviews", "Can moderate reviews"),  # для модераторов
        ]

    def save(self, *args, **kwargs):
        if not self.username:
            last_review = Review.objects.filter(movie=self.movie).order_by('-id').first()
            next_index = 0
            if last_review:
                last_username = last_review.username
                if last_username.startswith('testUser'):
                    try:
                        next_index = int(last_username.replace('testUser', '')) + 1
                    except:
                        next_index = last_review.id
            self.username = f"testUser{next_index}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.movie.title}"