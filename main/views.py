from django.shortcuts import render

def index(request):
  return render(request, 'index.html', {})

def category(request, id):
  return render(request, 'index.html', {})