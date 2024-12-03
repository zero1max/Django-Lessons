from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, template_name='page/index.html')

def users(request):
    return render(request, template_name='page/user.html')