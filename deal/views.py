from django.shortcuts import render

def index(request):
    return render(request, 'deals/deals.html')

def deal(request):
  return render(request, 'deals/deal.html')