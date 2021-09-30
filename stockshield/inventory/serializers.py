from rest_framework import serializers
from .models import Inventory

class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields =('id','owner','name','category','cost_price','selling_price','description','stock_quantity',)

