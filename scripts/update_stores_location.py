import os
os.environ["GOOGLE_API_KEY"]="AIzaSyD314-K42HiRw7wPNJmsqLE4wJgxDVpgWA"
import geocoder
from pos.models import Store

stores = Store.objects.all()
for store in stores:
    if (not store.latitude):
        try:
            g = geocoder.google(store.addr1+","+store.addr2+","+store.addr3+","+store.city+","+store.state+","+store.pincode)
            store.latitude=g.latlng[0]
            store.longitude=g.latlng[1]
            #print(store.position)
            store.save()
        except:
            print("Not Updated: " + store.name)
