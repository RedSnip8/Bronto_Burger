from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='deals'),
    path('deal', views.deal, name='deal'),
]