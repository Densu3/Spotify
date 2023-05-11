from django.shortcuts import render, redirect
from .models import Post

def index(request):
    news = Post.objects.order_by('-created_at') [:3]
    return render(request, 'spotify_app/index.html', {'news' : news})