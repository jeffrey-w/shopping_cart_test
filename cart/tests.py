from decimal import Decimal
from django.test import TestCase


from cart.models import Cart, Item, Product

class ModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='test', description='test', vendor='test', price=Decimal('999.99'))
        self.cart = Cart.objects.create(user='test')

    def test_empty_cart_has_zero_count(self):
        self.assertEqual(0, self.cart.count)

    def test_empty_cart_has_zero_total(self):
        self.assertEqual(0, self.cart.total)
    
    def test_non_empty_cart_has_expected_count(self):
        count = self.cart.count
        item = self.cart.add(self.product, 1)
        self.assertEquals(count + item.quantity, self.cart.count)
    
    def test_non_empty_cart_has_expected_total(self):
        item = self.cart.add(self.product, 1)
        self.assertEqual(self.product.price * item.quantity, self.cart.total)
    
    def test_attempting_to_remove_from_empty_cart_has_no_effect(self):
        self.assertEqual((0, {}), self.cart.remove(1))
    
    def test_removing_from_non_empty_cart_has_expected_effect(self):
        item = self.cart.add(self.product, 1)
        count, removed = self.cart.remove(item.id)
        self.assertEqual(1, count)
        self.assertEqual(1, removed['cart.Item'])
    
    def test_updating_item_quantity_has_expected_effect_on_cart_count_and_total(self):
        item = Item.objects.create(quantity=1, product=self.product, cart=self.cart)
        count = self.cart.count
        self.cart.update(item.id, 2)
        self.assertEqual(count + 1, self.cart.count)
        self.assertEqual(self.product.price * 2, self.cart.total)
