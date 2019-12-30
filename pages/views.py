from django.shortcuts import render
from django.views.generic import TemplateView

class homePageView(TemplateView):
        template_name = 'adminlte/index.html'

class homePage1View(TemplateView):
        template_name = 'adminlte/dashboard1.html'

class homePage2View(TemplateView):
        template_name = 'adminlte/dashboard2.html'

class homePage3View(TemplateView):
        template_name = 'adminlte/dashboard3.html'



# Create your views here.
