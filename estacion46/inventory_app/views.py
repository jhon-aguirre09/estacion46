from django.shortcuts import render, get_object_or_404,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib import messages
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                            BSModalUpdateView,
                                            BSModalDeleteView)

from .forms import InventoryForm

from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class InventoryList(LoginRequiredMixin,generic.ListView):
    model = models.Inventory
    context_object_name = 'products_inv'

class InventoryCreateView(BSModalCreateView):
    model = models.Inventory
    form_class = InventoryForm
    template_name = 'inventory_app/inventory_form.html'
    success_url = reverse_lazy('inventory:all')

class InventoryUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Inventory
    form_class = InventoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inventory:all')

class InventoryDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = models.Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_message = 'Success: Inventory was deleted.'
    success_url = reverse_lazy('inventory:all')
