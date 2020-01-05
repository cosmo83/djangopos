import csv
from pos.models import *

with open('./scripts/products.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         hsncode = TaxesGST.objects.get(hsnname=row[3])
         if(int(row[4].strip())):
             product = Product(item_code=row[1].strip(),name=row[0].strip(),code=row[2].strip(),hsncode=hsncode,is_product_serial=True)
             product.save()
         else:
             product = Product(item_code=row[1].strip(),name=row[0].strip(),code=row[2].strip(),hsncode=hsncode,is_product_serial=False)
             product.save()
       except:
         pass
