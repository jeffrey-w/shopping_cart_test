from decimal import Decimal
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    vendor = models.CharField(max_length=255) # In production, this would most likely be a foreign key to a vendor table.
    # pic = models.ImageField(upload_to='static') TODO implement image uploads.
    price = models.DecimalField(max_digits=16, decimal_places=2) # Use decimal for currency for arithmetic precision.

class Cart(models.Model):
    user = models.CharField(max_length=32) # In production, this would most likely be a foreign key to a user table.

    @property
    def count(self) -> int:
        return sum(map(lambda item: item.quantity, self.item_set.all()))

    @property
    def total(self) -> Decimal:
        return sum(map(lambda item: item.price, self.item_set.all()))

    @property
    def items(self) -> models.QuerySet:
        return self.item_set.all()

    def add(self, product: Product, quantity: int) -> None:
        self.item_set.create(product=product, quantity=quantity)

class Item(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()

    @property
    def price(self) -> Decimal:
        return self.product.price * self.quantity
