from django.db import models
from . import PaymentStatus
from pos.models import Sale

# Create your models here.
class BasePayment(models.Model):
    driver = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=PaymentStatus.CHOICES,default=PaymentStatus.WAITING)
    #: Creation date and time
    created = models.DateTimeField(auto_now_add=True)
    #: Date and time of last modification
    modified = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Sale,on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    captured_amount = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
