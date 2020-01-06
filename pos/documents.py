from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Inventory, Product,Store

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
     class Index:
         name="inventory"
