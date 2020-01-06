from django.db import models
from organizations.models import Organization
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
import re



# Create your models here.
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

sale_status = ((0,"Sale Completed"),(1,"Sale in Progress"),(2,"Sale Cancelled"))
inv_status = ((0,"In Store"),(1,"Sold"),(2,"In Transit"))
pricelist_type=(("sale","Sale"),("cost","Cost"))
def validate_product_name(prodname):
    regex_string = r'^\w[\w ]*$'
    search = re.compile(regex_string).search
    result = bool(search(prodname))
    if not result:
        raise ValidationError("Please only use letters, "
                              "numbers and underscores or spaces. "
                              "The name cannot start with a space.")


class Store(Organization):
        code = models.CharField("Store ID",max_length=10,unique=True)
        addr1 = models.CharField("Address 1",max_length=200)
        addr2 = models.CharField("Address 2",max_length=200)
        addr3 = models.CharField("Address 3",max_length=200)
        city = models.CharField("City",max_length=100)
        state = models.CharField("State",max_length=80,choices=state_choices)
        pincode = models.CharField("Pin-Code",max_length=6)
        is_sale_location = models.BooleanField(default=True)
        latitude = models.DecimalField("Latitude", blank=True, null=True,max_digits=22,decimal_places=10)
        longitude = models.DecimalField("Longitude", blank=True, null=True,max_digits=22,decimal_places=10)
        def __str__(self):
            return self.code+"-"+self.name

        @property
        def location_field_indexing(self):
            return {
                'lat': self.latitude,
                'lon': self.longitude,
                }

        class Meta:
          verbose_name = 'Storage Location'
          verbose_name_plural = 'Storage Locations'


class Sale(TimeStampedModel):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE, limit_choices_to={'is_sale_location':True,'is_deleted':False})

    status = models.IntegerField("Sale Status",default=False,choices=sale_status)



class TaxesGST(models.Model):
    hsnname = models.CharField("HSN Code",max_length=20)
    taxrate = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.hsnname


class Product(models.Model):
    name = models.CharField(max_length=100,
                            validators=[validate_product_name],db_index=True)
    item_code = models.CharField("Item Code",max_length=50,primary_key=True,db_index=True)
    code = models.CharField("UPC Code",max_length=50, null=True, blank=True)
    hsncode = models.ForeignKey(TaxesGST,on_delete=models.CASCADE)
    is_product_serial = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def hsnname(self):
        return self.hsncode.hsnname

    def hsnigst(self):
        return self.hsncode.taxrate


    #If the product is not having a serial number, its assumed to have a batch number. If the batchnumber = null, then no batches

class Inventory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete = models.CASCADE)
    count = models.DecimalField(max_digits=7,decimal_places=2)
    serialbatchnumber = models.CharField("Serial / Batch Number",max_length=50,null=True,blank=True)
    status = models.IntegerField("Status",choices=inv_status,default=0)
    class Meta:
      verbose_name = 'Inventory'
      verbose_name_plural = 'Inventory Lines'

    @property
    def sale_price(self):
        if(self.serialbatchnumber is not None):
            prices = PriceList.objects.filter(product=self.product,type='sale',serialbatchnumber=self.serialbatchnumber)
            if (prices.count() == 0):
                if (PriceList.objects.filter(product=self.product,type='sale',serialbatchnumber=None).count() == 1):
                    return PriceList.objects.filter(product=self.product,type='sale',serialbatchnumber=None)[0].price
                else:
                    return 1.00 # If the pricelist is not having the product, then it will be showing 1.00 Re
            if (prices.count() == 1):
                return prices[0].price
        else:
            return PriceList.objects.filter(product=self.product,type='sale',serialbatchnumber=None)[0].price

    def productname(self):
        return self.product.name

    def storename(self):
        return self.store.name

    def __str__(self):
        return self.product.name+"-"+self.store.name

class PriceList(models.Model):
    type=models.CharField("Price List Type",choices=pricelist_type,max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    serialbatchnumber = models.CharField("Serial/Batch Number",max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        if (self.serialbatchnumber is not None):
            return self.product.name+"---"+self.serialbatchnumber
        else:
            return self.product.name


class SaleLine(models.Model):
    saleorder = models.ForeignKey(Sale,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2,default=0)
