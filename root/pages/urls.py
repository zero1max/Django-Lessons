from django.urls import path
from pages.views import home, posts

urlpatterns = [
    path('home', home, name='home'),
    path('post', posts, name='post')  # Add a new URL for users
]