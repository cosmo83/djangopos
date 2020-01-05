from .models import Sale,SaleLine, Inventory
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import InvDocument

class InvDocSerializer(DocumentSerializer):
    product = serializers.SerializerMethodField()
    storename = serializers.CharField()
    sale_price = serializers.FloatField()
    class Meta(object):
        fields =(
            'serialbatchnumber',
            'count'
        )
        document = InvDocument

    def get_product(self,obj):
        if(obj.product):
            print(obj.product)
            return {'name':obj.product.name,'hsncode':obj.product.hsnname,'hsntax':obj.product.hsnigst}
        else:
            return {}


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
