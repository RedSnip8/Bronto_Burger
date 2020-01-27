from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='menu'),
  path('<int:item_id>', views.item, name='nutrition')
]