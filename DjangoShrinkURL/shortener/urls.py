from django.urls import path
from .views import URLShortenerView, LoginView, register, dashboard, logout, delete_url

urlpatterns = [
    path('', URLShortenerView.as_view(), name='urlshortener'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('delete_url/<int:url_id>/', delete_url, name='delete_url'),
    path('dashboard/', dashboard, name='dashboard'),
    path('<str:short_url>', URLShortenerView.as_view(), name='urlredirect'),
]
