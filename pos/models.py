from django.db import models
from organizations.models import Organization
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
import re

# Create your models here.
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

sale_status = ((0,"Sale Completed"),(1,"Sale in Progress"),(2,"Sale Cancelled"))

def validate_product_name(prodname):
    regex_string = r'^\w[\w ]*$'
    search = re.compile(regex_string).search
    result = bool(search(prodname))
    if not result:
        raise ValidationError("Please only use letters, "
                              "numbers and underscores or spaces. "
                              "The name cannot start with a space.")


class Store(Organization):
        code = models.CharField("Store ID",max_length=10)
        addr = models.TextField("Address")
        city = models.CharField("City",max_length=100)
        state = models.CharField("State",max_length=80,choices=state_choices)
        pincode = models.CharField("Pin-Code",max_length=6)
        gstn = models.CharField("GSTN Number",max_length=20,blank=True)
        is_sale_location = models.BooleanField(default=True)
        is_deleted = models.BooleanField(default=False)

        class Meta:
          verbose_name = 'Storage Location'
          verbose_name_plural = 'Storage Locations'

class Sale(TimeStampedModel):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE, limit_choices_to={'is_sale_location':True,'is_deleted':False})
    
    status = models.IntegerField("Sale Status",default=False,choices=sale_status)


    

class Product(models.Model):
    name = models.CharField(max_length=100,
                            validators=[validate_product_name])
    item_code = models.CharField("Item Code",max_length=50, unique=True)
    code = models.CharField("UPC Code",max_length=50, unique=True, null=True, blank=True)
    hsncode = models.CharField("HSN Code",max_length=20)
    sell_price = models.DecimalField(max_digits=7, decimal_places=2)
     
class SaleLine(models.Model):
    saleorder = models.ForeignKey(Sale,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2,default=0)
