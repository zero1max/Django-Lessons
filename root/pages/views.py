from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return render(request, template_name='page/index.html')

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template_name='page/post.html', context=context)