from django.shortcuts import render
from django.http import Http404

# Категории новостей
CATEGORIES = [
    {'name': 'Фильмы', 'slug': 'films'},
    {'name': 'Спорт', 'slug': 'sports'},
    {'name': 'Технологии', 'slug': 'tech'},
]

# Главная страница — список категорий
def home(request):
    return render(request, 'news/home.html', {'categories': CATEGORIES})

# Новости
NEWS = [
    {'id': 1, 'title': 'Оскар 2026', 'image': 'news/images/image.png', 'category': 'films', 'text': 'Полный текст новости о фильмах...'},
    {'id': 2, 'title': 'Футбол: Чемпионат', 'image': 'news/images/image.png', 'category': 'sports', 'text': 'Текст новости о футболе...'},
    {'id': 3, 'title': 'Новые технологии', 'image': 'news/images/image.png', 'category': 'tech', 'text': 'Текст новости о технологиях...'},
]

# Страница категории
def category(request, slug):
    filtered_news = [n for n in NEWS if n['category'] == slug]
    category_name = next((c['name'] for c in CATEGORIES if c['slug'] == slug), slug)
    return render(request, 'news/category.html', {'news_list': filtered_news, 'category_name': category_name})

# Страница новости
def news_detail(request, news_id):
    news_item = next((n for n in NEWS if n['id'] == news_id), None)
    if not news_item:
        raise Http404("Новость не найдена")
    return render(request, 'news/news_detail.html', {'news': news_item})