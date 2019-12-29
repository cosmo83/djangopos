from django.contrib import admin
from .models import Product,Store,Sale,SaleLine


class SaleAdmin(admin.ModelAdmin):
    readonly_fields=('id','created','modified')

# Register your models here.
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleLine)

