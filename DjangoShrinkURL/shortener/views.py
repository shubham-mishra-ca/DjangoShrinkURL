from django.shortcuts import render
from django.views import View
from .models import URL

class URLShortenerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/index.html')

    def post(self, request, *args, **kwargs):
        original_url = request.POST['original_url']
        url, created = URL.objects.get_or_create(original_url=original_url)
        return render(request, 'shortener/index.html', {'url': url})