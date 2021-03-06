from .models import Sale,SaleLine, Inventory,Customer
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import InvDocument



class InvDocSerializer(DocumentSerializer):
    product = serializers.SerializerMethodField()
    store = serializers.SerializerMethodField()
    sale_price = serializers.FloatField()
    class Meta(object):
        fields =(
            'serialbatchnumber',
            'count'
        )
        document = InvDocument

    def get_store(self,obj):
        if(obj.store):
            return {'name':obj.store.name}

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

class CustomerSerializer(serializers.ModelSerializer):
    custname = serializers.CharField(source='name')
    custphone = serializers.CharField(source='phonenumber')
    custemail = serializers.CharField(source='email',required=False,default='')

    class Meta:
        model=Customer
        fields = ('custname','custphone','custemail')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id','store','employee','status']

class SaleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleLine
        fields = ['saleorder','product','quantity','price','discount']
