from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views import View
from .forms import LoginForm
from .models import URL
from django.contrib.auth import logout as django_logout
from django.contrib import messages



class URLShortenerView(View):
    def get(self, request, *args, **kwargs):
        if 'short_url' in kwargs:
            short_url = kwargs['short_url']
            try:
                url = URL.objects.get(short_url=short_url)
                url.times_visited += 1
                url.save()
                return redirect(url.original_url)
            except URL.DoesNotExist:
                return render(request, 'shortener/index.html', {'error': 'This short URL does not exist.'})
        else:
            return render(request, 'shortener/index.html')
    
    def post(self, request, *args, **kwargs):
        original_url = request.POST['original_url']
        validate = URLValidator()
        try:
            validate(original_url)
        except ValidationError:
            return render(request, 'shortener/index.html', {'error': 'The provided URL is not valid.'})

        url, created = URL.objects.get_or_create(original_url=original_url)

        if not created and url.user is None and request.user.is_authenticated:
            url.user = request.user
            url.save()

        if created:
            messages.success(request, 'URL successfully shortened.')
        else:
            if request.user.is_authenticated:
                if url.user == request.user:
                    messages.info(request, 'URL already shortened earlier by you.')
                else:
                    messages.success(request, 'URL successfully shortened.')

        return redirect('success', url_id=url.id)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'shortener/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('urlshortener')
        else:
            return render(request, 'shortener/login.html', {'form': form})

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

def logout(request):
    django_logout(request)
    return redirect('login') 

def delete_url(request, url_id):
    if request.user.is_authenticated:
        url = get_object_or_404(URL, id=url_id, user=request.user)
        url.delete()
    return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        urls = URL.objects.filter(user=request.user)
        return render(request, 'shortener/dashboard.html', {'urls': urls})
    else:
        return redirect('login')

def success(request, url_id):
    url = get_object_or_404(URL, id=url_id)
    return render(request, 'shortener/success.html', {'url': url})