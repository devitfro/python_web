import time
from django.http import JsonResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests = {}

    def __call__(self, request):
        if request.path == '/restricted-area/':
            ip = request.META.get('REMOTE_ADDR')
            now = time.time()

            if ip not in self.requests:
                self.requests[ip] = []

            # оставить только последние 60 сек
            self.requests[ip] = [
                t for t in self.requests[ip] if now - t < 60
            ]

            if len(self.requests[ip]) >= 5:
                return JsonResponse({'error': 'Too many requests'}, status=429)

            self.requests[ip].append(now)

        return self.get_response(request)