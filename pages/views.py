from django.shortcuts import render

def index(request):
    return render(request, 'templates/pages/index.html')

def about(request):
    return render(request, 'templates/pages/about.html')

def bronto_app(request):
    return render(request, 'templates/pages/bronto_app.html')

def contact(request):
    return render(request, 'templates/pages/contact.html')

def faq(request):
    return render(request, 'templates/pages/faq.html')

def investments(request):
    return render(request, 'templates/pages/investments.html')

def privacy(request):
    return render(request, 'templates/pages/privacy.html')

def sitemap(request):
    return render(request, 'templates/pages/sitemap.html')

def terms(request):
    return render(request, 'templates/pages/terms.html')