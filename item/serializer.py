from rest_framework import serializers
from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_qty', 'item_unit', 'wholesale_rate',
                  'retail_rate', 'outside_rate', 'product_charge', 'vehicle_rent_wholesale_rate',
                  'vehicle_rent_outside_rate', 'vehicle_rent_retail_rate', 'vehicle_rent_factory_rate',
                  'created_at', 'created_by', 'updated_at', 'updated_by']
