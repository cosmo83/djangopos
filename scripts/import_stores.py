import csv
from pos.models import *

with open('./scripts/storeap.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         store = Store(code=row[0].strip(),name=row[1].strip(),addr1=row[2].strip(),addr2=row[3].strip(),addr3=row[4].strip(),pincode=row[5].strip(),city=row[6].strip(),state=row[7].strip())
         store.save()
       except:
         pass


with open('./scripts/storetg.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         store = Store(code=row[0].strip(),name=row[1].strip(),addr1=row[2].strip(),addr2=row[3].strip(),addr3=row[4].strip(),pincode=row[5].strip(),city=row[6].strip(),state=row[7].strip())
         store.save()
       except:
         pass
