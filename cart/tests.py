from decimal import Decimal, getcontext
from django.test import TestCase

from cart.models import Cart, Product

class ModelTests(TestCase):

    def setUp(self):
        context = getcontext()
        context.prec = 2
        self.product = Product.objects.create(name='test', description='test', vendor='test', price=999.99)
        self.cart = Cart.objects.create(user='test')

    def test_empty_cart_has_zero_count(self):
        self.assertEqual(0, self.cart.count)

    def test_empty_cart_has_zero_total(self):
        self.assertEqual(0, self.cart.total)
    
    def test_non_empty_cart_has_expected_count(self):
        count = self.cart.count
        self.cart.add(self.product, 1)
        self.assertEquals(count + 1, self.cart.count)
    
    def test_non_empty_cart_has_expected_total(self):
        self.cart.add(self.product, 2)
        self.assertEqual(Decimal(999.99) * 2, self.cart.total)
    
    def test_updating_item_quantity_has_expected_effect_on_cart_count_and_total(self):
        self.cart.add(self.product, 1)
        count = self.cart.count
        item = self.cart.items.first()
        item.quantity = 2
        item.save()
        self.assertEqual(count + 1, self.cart.count)
        self.assertEqual(Decimal(999.99) * 2, self.cart.total)
