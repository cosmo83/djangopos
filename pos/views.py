from django.shortcuts import render
from .models import Sale,SaleLine, Inventory,Product
# Create your views here.
from rest_framework import viewsets

from .serializers import SaleSerializer,SaleLineSerializer,InvSerializer
from django.views.generic import TemplateView
from django.http import JsonResponse

def productsearch_list(request,searchcode):
	if request.method == 'GET':
		products = Product.objects.filter(name__icontains=searchcode)
		inventorylines = Inventory.objects.filter(product__in=products)
		serializer = InvSerializer(inventorylines,many=True)
		return JsonResponse(serializer.data,safe=False)


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
