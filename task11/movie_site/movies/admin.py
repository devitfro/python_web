# admin.py
from django.contrib import admin
from .models import Movie, Genre, Review

# Admin для отзывов
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'movie', 'text_short', 'created_at')
    list_filter = ('created_at', 'movie')
    search_fields = ('username', 'text', 'movie__title')
    ordering = ('-created_at',)

    def text_short(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    text_short.short_description = 'Текст відгуку'

    # Ограничение доступа для модераторов
    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('movies.can_moderate_reviews') or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('movies.can_moderate_reviews') or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        # Добавлять можно только суперюзеру
        return request.user.is_superuser
      
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'country', 'rating', 'reviews_count', 'genres_list')
    list_filter = ('release_date', 'country', 'rating', 'genre')
    search_fields = ('title', 'description')
    ordering = ('-release_date',)

    filter_horizontal = ('genre',)  # удобный вид для ManyToMany

    def reviews_count(self, obj):
        return obj.reviews.count()
    reviews_count.short_description = 'Количество отзывов'

    def genres_list(self, obj):
        return ", ".join([g.name for g in obj.genre.all()])
    genres_list.short_description = 'Жанры'