from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='menu'),
  path('item', views.item, name='nutrition')
]