from django.shortcuts import render
from .models import Sale,SaleLine, Inventory,Product,Store,Customer
# Create your views here.
from rest_framework import viewsets

from .serializers import SaleSerializer,SaleLineSerializer,InvSerializer, InvDocSerializer,CustomerSerializer
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from .documents import InvDocument,CustomerDocument

def customersearch_list(request,searchcode):
	if request.method == 'GET':
		custlines = CustomerDocument.search().query("query_string",query="*"+searchcode+"*",fields=['name','phonenumber'])
		serializer = CustomerSerializer(custlines[0:custlines.count()],many=True)
		return HttpResponse(json.dumps(serializer.data))


def productsearch_list(request,searchcode):
	if request.method == 'GET':
		invlines = InvDocument.search().query("query_string",query="*"+searchcode+"*",fields=['product.name','serialbatchnumber']).query("match",status=0)
		serializer = InvDocSerializer(invlines[0:invlines.count()],many=True)
		return HttpResponse(json.dumps(serializer.data))

def productsearch_list_store(request,searchcode):
	if request.method == 'GET':
		storecode = Store.objects.get(id=request.session['store_id']).code
		invlines = InvDocument.search().query("query_string",query="*"+searchcode+"*",fields=['product.name','serialbatchnumber']).query("match",store__code=storecode).query("match",status=0)
		serializer = InvDocSerializer(invlines[0:invlines.count()],many=True)
		return HttpResponse(json.dumps(serializer.data))

def idoc_handler(request):
	if request.method == 'POST':
		print("Something got Posted")


class InventoryViewSet(viewsets.ModelViewSet):
	queryset = Inventory.objects.all()
	serializer_class = InvSerializer

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class SaleViewSet(viewsets.ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

class SaleLineViewSet(viewsets.ModelViewSet):
	queryset = SaleLine.objects.all()
	serializer_class = SaleLineSerializer


class SalesPageView(TemplateView):
    template_name = 'adminlte/order.html'
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['storename']=Store.objects.get(id=self.request.session['store_id']).name
       context['stores'] = Store.objects.filter(users=self.request.user.id)
       context['userid'] = self.request.user.id
       return context
