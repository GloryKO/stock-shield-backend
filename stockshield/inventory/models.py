from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Inventory(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    category =models.CharField(max_length=250)
    cost_price =models.DecimalField(decimal_places=2,max_digits=10)
    selling_price =models.DecimalField(decimal_places=2, max_digits=10)
    description =models.TextField(blank=True)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name