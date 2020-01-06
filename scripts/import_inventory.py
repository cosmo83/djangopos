import csv
from pos.models import *
from itertools import islice

with open('./scripts/inv.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         store = Store.objects.get(code=row[0].strip())
         product = Product.objects.get(item_code=row[1].strip())
         inv = Inventory(product=product,store=store,serialbatchnumber=row[2].strip(),count=1.0)
         print("Importing "+row[1])
         inv.save()
       except:
         print("Not Importing "+row[1])
         pass
