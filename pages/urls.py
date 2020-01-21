from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('bronto_app', views.bronto_app, name='bronto_app'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('investments', views.investments, name='investments'),
    path('privacy', views.privacy, name='privacy'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('terms', views.terms, name='terms'),
]

