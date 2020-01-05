import csv
from pos.models import *

with open('./scripts/hsncodes.csv') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
       try:
         hsncode = TaxesGST(hsnname=row[1],taxrate=row[2])
         hsncode.save()
       except:
         pass
