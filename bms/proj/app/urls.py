from django.urls import path
from .views import chat_view,home

urlpatterns = [
    path('', home, name='home'),
    path('/Anon', chat_view, name='chat'),
]