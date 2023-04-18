from django.shortcuts import render

def index(request):
    return render(request, 'spotify_app/index.html')