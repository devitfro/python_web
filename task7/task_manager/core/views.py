from django.http import JsonResponse
from django.shortcuts import redirect, render
from .cache import get_from_cache, set_to_cache
from .data_store import data_dict
import json


def get_item(request, item_id):
    cache_key = f"item_{item_id}"
    cached = get_from_cache(cache_key)

    if cached:
        return JsonResponse({'source': 'cache', 'data': cached})

    data = {'id': item_id, 'name': f'Item {item_id}'}
    set_to_cache(cache_key, data)

    return JsonResponse({'source': 'db', 'data': data})


def process_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name', '').capitalize()
            age = int(data.get('age'))

            return JsonResponse({'name': name, 'age': age})

        except Exception:
            return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)


def check_device(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    if 'mobile' in user_agent:
        return redirect('/mobile-page/')

    return JsonResponse({'message': 'Добро пожаловать на сайт!'})


def mobile_page(request):
    return render(request, 'core/mobile.html')


def get_data(request, key):
    if key in data_dict:
        return JsonResponse({key: data_dict[key]})

    return JsonResponse({'error': 'Not found'}, status=404)


def update_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data_dict.update(data)

            return JsonResponse({'status': 'updated', 'data': data_dict})
        except Exception:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)


def restricted_view(request):
    return JsonResponse({'message': 'Access OK'})