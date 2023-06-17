from django.urls import path
from .views import URLShortenerView, LoginView, register, dashboard, logout

urlpatterns = [
    path('', URLShortenerView.as_view(), name='urlshortener'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),  
]
