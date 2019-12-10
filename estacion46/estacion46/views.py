from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def HomePage(request):
     return HttpResponseRedirect(reverse('dashboard'))

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
