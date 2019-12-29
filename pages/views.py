from django.shortcuts import render
from django.views.generic import TemplateView

class homePageView(TemplateView):
        template_name = 'registration/index.html'

class SalesPageView(TemplateView):
        template_name = 'registration/order.html'

# Create your views here.
