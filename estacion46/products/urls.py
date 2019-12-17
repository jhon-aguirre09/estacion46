from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(),name='all'),
    path('nuevo/', views.ProductCreateView.as_view(),name='create_product'),
    path('editar/<int:pk>', views.ProductUpdateView.as_view(), name='edit'),
    path('borrar/<int:pk>', views.ProductDeleteView.as_view(), name='delete'),
]
