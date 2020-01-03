from .models import Sale,SaleLine, Inventory
from rest_framework import serializers


class InvSerializer(serializers.ModelSerializer):
     productname = serializers.CharField(source='product.name')
     storename = serializers.CharField(source='store.name')
     sale_price  = serializers.ReadOnlyField()

     class Meta:
         model=Inventory
         fields = ('productname','storename','count','serialbatchnumber','sale_price')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id','store','employee','status']

class SaleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleLine
        fields = ['saleorder','product','quantity','price','discount']
