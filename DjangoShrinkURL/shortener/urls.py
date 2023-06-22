from django.urls import path
from .views import URLShortenerView, LoginView, register, logout, dashboard, delete_url, success

urlpatterns = [
    path('', URLShortenerView.as_view(), name='urlshortener'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('delete_url/<int:url_id>/', delete_url, name='delete_url'),
    path('<str:short_url>/', URLShortenerView.as_view(), name='urlshortener'),
    path('success/<int:url_id>/', success, name='success'), 
]
