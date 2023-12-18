from django.shortcuts import render

# Create your views here or end points

def index(request, *arg, **kwargs):
    return render(request, 'frontend/index.html')
