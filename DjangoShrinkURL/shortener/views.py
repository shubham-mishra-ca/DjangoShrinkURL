from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views import View
from .models import URL

class URLShortenerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/index.html')

    def post(self, request, *args, **kwargs):
        original_url = request.POST['original_url']
        validate = URLValidator()
        try:
            validate(original_url)
        except ValidationError:
            return render(request, 'shortener/index.html', {'error': 'The provided URL is not valid.'})

        url, created = URL.objects.get_or_create(original_url=original_url)
        return render(request, 'shortener/index.html', {'url': url})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('urlshortener')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})