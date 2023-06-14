from django.urls import path
from .views import URLShortenerView 

urlpatterns = [
    path('', URLShortenerView.as_view(), name='urlshortener'),
]
