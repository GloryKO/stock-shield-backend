from django.test import TestCase
from inventory.models import Inventory
from django.contrib.auth import get_user_model
User = get_user_model()
class InventoryTestModel(TestCase):

    def test_model_str(self):
        name  = Inventory.objects.create(owner = User.objects.create(),name="hisense",cost_price=10.0,selling_price=20,stock_quantity=4)
        self.assertEqual(str(name),"hisense")