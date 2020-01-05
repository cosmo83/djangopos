from django.shortcuts import render
from .models import Sale,SaleLine, Inventory,Product
# Create your views here.
from rest_framework import viewsets

from .serializers import SaleSerializer,SaleLineSerializer,InvSerializer, InvDocSerializer
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from .documents import InvDocument

def productsearch_list(request,searchcode):
	if request.method == 'GET':
		invlines = InvDocument.search().query("multi_match",query=searchcode,fields=['product.name','serialbatchnumber'])
		serializer = InvDocSerializer(invlines[0:invlines.count()],many=True)
		return HttpResponse(json.dumps(serializer.data))



class InventoryViewSet(viewsets.ModelViewSet):
	queryset = Inventory.objects.all()
	serializer_class = InvSerializer



class SaleViewSet(viewsets.ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

class SaleLineViewSet(viewsets.ModelViewSet):
	queryset = SaleLine.objects.all()
	serializer_class = SaleLineSerializer


class SalesPageView(TemplateView):
        template_name = 'adminlte/order.html'
