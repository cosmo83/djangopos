import csv
from pos.models import *

with open('./scripts/storeap.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         store = Store(code=row[0].strip(),name=row[1].strip(),addr1=row[2].strip(),addr2=row[3].strip(),pincode=row[4].strip(),city=row[5].strip(),state=row[6].strip())
         store.save()
       except:
         pass
