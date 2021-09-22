from django.db import models
from rest_framework import serializers
from .models import CustomUser
from .models import Product_Inventory

class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Inventory
        fields =('id','owner','name','category','cost_price','selling_price','description','stock_quantity',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','username','business_name','phone_number',)

