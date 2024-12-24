from django.urls import path
from .views import post_detail, PostListView

app_name = 'blog'

urlpatterns = [
    # Post views
    # path('', views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
]