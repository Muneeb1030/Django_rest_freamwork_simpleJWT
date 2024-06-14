from django.urls import path

from .views import get_user_all, delete_user_all, create_user, login

urlpatterns = [
    path('', get_user_all, name='get-user-all'),
    path('delete-all', delete_user_all, name='delete-user-all'),
    path('create-user', create_user, name='create-user'),
    path('login', login, name='login')
]
