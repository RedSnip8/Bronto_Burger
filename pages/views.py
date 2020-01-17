from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def bronto_app(request):
    return render(request, 'pages/bronto_app.html')

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def investments(request):
    return render(request, 'pages/investments.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def sitemap(request):
    return render(request, 'pages/sitemap.html')

def terms(request):
    return render(request, 'pages/terms.html')