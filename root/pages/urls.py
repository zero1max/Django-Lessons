from django.urls import path
from pages.views import home, users

urlpatterns = [
    path('home', home, name='home'),
    path('users', users, name='users')  # Add a new URL for users
]