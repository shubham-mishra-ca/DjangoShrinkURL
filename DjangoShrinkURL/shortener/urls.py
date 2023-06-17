from django.contrib import admin
from django.urls import path
from .views import URLShortenerView, LoginView, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', URLShortenerView.as_view(), name='urlshortener'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
]