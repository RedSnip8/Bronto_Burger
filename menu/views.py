from django.shortcuts import render

def index(request):
  return render(request, 'menu/menu.html')

def item(request):
  return render(request, 'menu/nutrition.html')
