from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryList.as_view(),name='all'),
    path('nuevo/', views.CreateInventory.as_view(),name='create')
]
