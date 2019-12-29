from .models import Sale,SaleLine
from rest_framework import serializers

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id','store','employee','status']

class SaleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleLine
        fields = ['saleorder','product','quantity','price','discount'] 
