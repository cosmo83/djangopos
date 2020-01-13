from django.contrib import admin
from .models import Product,Store,Sale,SaleLine,Inventory,PriceList,TaxesGST,Customer
from import_export.admin import ImportExportModelAdmin
from django.conf import settings

class SaleAdmin(admin.ModelAdmin):
    readonly_fields=('id','created','modified')

@admin.register(TaxesGST)
class TaxesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('/static/admin/css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                '/static/admin/js/admin/location_picker.js',
            )
# Register your models here.

admin.site.register(Inventory)
admin.site.register(PriceList)

admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleLine)
admin.site.register(Customer)
