from django.urls import path
from .views import URLShortenerView, LoginView, register, dashboard 

urlpatterns = [
    path('', URLShortenerView.as_view(), name='urlshortener'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),  
]
