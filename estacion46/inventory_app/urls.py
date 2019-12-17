from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryList.as_view(),name='all'),
    path('nuevo/', views.InventoryCreateView.as_view(),name='create_product_inv'),
    path('editar/<int:pk>', views.InventoryUpdateView.as_view(), name='edit'),
    path('borrar/<int:pk>', views.InventoryDeleteView.as_view(), name='delete'),
]
