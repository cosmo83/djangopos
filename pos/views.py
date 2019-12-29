from django.shortcuts import render
from .models import Sale,SaleLine
# Create your views here.
from rest_framework import viewsets

from .serializers import SaleSerializer,SaleLineSerializer


class SaleViewSet(viewsets.ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

class SaleLineViewSet(viewsets.ModelViewSet):
	queryset = SaleLine.objects.all()
	serializer_class = SaleLineSerializer
