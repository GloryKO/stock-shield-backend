from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class CustomUser(AbstractUser):
    business_name = models.CharField(max_length=500,null=True, blank=True)
    phone_number = PhoneField(blank=True,help_text='Contact phone number')
    
class Product_Inventory(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    category =models.CharField(max_length=250)
    cost_price =models.DecimalField(decimal_places=2,max_digits=10)
    selling_price =models.DecimalField(decimal_places=2, max_digits=10)
    description =models.TextField(blank=True)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name