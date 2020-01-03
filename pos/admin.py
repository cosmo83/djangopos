from django.contrib import admin
from .models import Product,Store,Sale,SaleLine,Inventory,PriceList,TaxesGST
from import_export.admin import ImportExportModelAdmin

class SaleAdmin(admin.ModelAdmin):
    readonly_fields=('id','created','modified')

@admin.register(TaxesGST)
class TaxesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

# Register your models here.

admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(PriceList)

admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleLine)
