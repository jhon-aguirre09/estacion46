from django.shortcuts import render, get_object_or_404,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                            BSModalUpdateView,
                                            BSModalDeleteView)
from .forms import ProductForm

from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class ProductList(LoginRequiredMixin,generic.ListView):
    model = models.Product
    context_object_name = 'products'

class ProductCreateView(BSModalCreateView):
    template_name = 'products/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:all')

class ProductUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Product
    form_class = ProductForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products:all')

class ProductDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = models.Product
    template_name = 'products/product_confirm_delete.html'
    success_message = 'Success: Product was deleted.'
    success_url = reverse_lazy('products:all')
