from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Inventory, Product,Store, PriceList, Customer

pos_index = Index('pos')

pos_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@registry.register_document
class CustomerDocument(Document):
    class Django:
        model = Customer
        fields = [
            'name',
            'phonenumber',
            'email'
        ]
    class Index:
        name="customer"

@registry.register_document
class StoreDocument(Document):
     # Location
    location = fields.GeoPointField(attr='location_field_indexing')
    class Django:
        model = Store
        fields = [
            'name',
            'code'
        ]
    class Index:
        name="store"

@registry.register_document
class ProductDocument(Document):
    hsnname = fields.TextField()
    hsnigst = fields.DoubleField()
    class Django:
        model = Product
        fields = [
            'name',
            'item_code'
        ]
    class Index:
        name="product"


@registry.register_document
class InvDocument(Document):
#     productname = fields.TextField()
     store = fields.ObjectField(properties={
        'name':fields.TextField(),
        'code':fields.TextField(),
        'location':fields.GeoPointField(attr='location_field_indexing')
     })
     product = fields.ObjectField(properties={
        'name': fields.TextField(),
        'hsnname': fields.TextField(),
        'hsnigst': fields.DoubleField(),
        'item_code':fields.TextField(),
     })
     sale_price = fields.TextField()

     class Django:
         model = Inventory
         fields = [
             'serialbatchnumber',
             'count',
             'status'
         ]
         related_models = [Store,Product,PriceList]

     def get_instances_from_related(self,related_instance):
         if isinstance(related_instance,Store):
             return related_instance.inventory_set.all()
         if isinstance(related_instance,Product):
             return related_instance.inventory_set.all()
         if isinstance(related_instance,PriceList):
             return related_instance.product.inventory_set.all()

     class Index:
         name="inventory"
