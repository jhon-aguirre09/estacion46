from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(),name='all'),
    path('nuevo/', views.CreateProduct.as_view(),name='create')
    re_path(r'editar/(?P<pk>\d+)/$',views.ClientUpdate.as_view(),name='product_edit'),
]
