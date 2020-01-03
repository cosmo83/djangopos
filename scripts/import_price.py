import csv
from pos.models import *

with open('./scripts/saleprice.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         product = Product.objects.get(item_code=row[0].strip())
         pricelist = PriceList(product=product,type="sale",price=row[1].strip(),serialbatchnumber=None)
         pricelist.save()
       except:
         pass
