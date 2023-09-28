from django.db import models
from app.models import Base
# Create your models here.


class Item(Base):
    item_name = models.CharField(null=False, blank=False, max_length=45)
    item_qty = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    item_unit = models.CharField(null=True, blank=True, max_length=8)
    wholesale_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    retail_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    outside_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    product_charge = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    vehicle_rent_wholesale_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    vehicle_rent_retail_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    vehicle_rent_outside_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    vehicle_rent_factory_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    wrapping = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'item'
