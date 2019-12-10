from django.shortcuts import render, get_object_or_404,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin

from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class ProductList(LoginRequiredMixin,generic.ListView):
    model = models.Product

class CreateProduct(LoginRequiredMixin,generic.CreateView):
    fields = ('nombre','codigo','codigo_Interno','presentacion','precio_Ingreso','precio_Venta')
    model = models.Product

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
