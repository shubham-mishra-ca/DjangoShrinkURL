from django.urls import path
from .views import URLShortenerView, register

urlpatterns = [
    path('register/', register, name='register'),
    path('', URLShortenerView.as_view(), name='urlshortener'),
]
