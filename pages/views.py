from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from pos.models import Store
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in




class homePageView(TemplateView):
        template_name = 'adminlte/index.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['storename']=Store.objects.get(id=self.request.session['store_id']).name
            context['stores'] = Store.objects.filter(users=self.request.user.id)
            return context


class homePage1View(TemplateView):
        template_name = 'adminlte/dashboard1.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['storename']=Store.objects.get(id=self.request.session['store_id']).name
            context['stores'] = Store.objects.filter(users=self.request.user.id)
            return context

class homePage2View(TemplateView):
        template_name = 'adminlte/dashboard2.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['storename']=Store.objects.get(id=self.request.session['store_id']).name
            context['stores'] = Store.objects.filter(users=self.request.user.id)
            return context

class homePage3View(TemplateView):
        template_name = 'adminlte/dashboard3.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['storename']=Store.objects.get(id=self.request.session['store_id']).name
            context['stores'] = Store.objects.filter(users=self.request.user.id)
            return context

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
        set_store_id(request)


def set_store_id(request):
        store_id=Store.objects.filter(users=request.user.id)[0].id
        request.session['store_id'] = store_id

def switch(request, storeid):
        request.session['store_id'] = storeid
        response = redirect(request.META.get('HTTP_REFERER'))
        return response

# Create your views here.
