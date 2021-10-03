from users.models import BusinessId
from django.test import TestCase


class BusinessModelTest(TestCase):

    def setUp(self):
        self.business = BusinessId.objects.create(business_name="bang and olufsen")

    def test_business_str(self):
        self.assertEqual(str(self.business),'bang and olufsen')

    def test_business_slug(self):
        self.assertIsNotNone(BusinessId.make_slug())

    def test_business_save(self):
        self.assertIsInstance(self.business, BusinessId)