from __future__ import annotations # For forward declared type hints.

from decimal import Decimal
from typing import Dict, Tuple
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    vendor = models.CharField(max_length=32) # In production, this would most likely be a foreign key to a vendor table.
    pic = models.ImageField(upload_to='products', default=None, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2) # Use decimal for currency for arithmetic precision.

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.CharField(max_length=32) # In production, this would most likely be a foreign key to a user table.

    @property
    def count(self) -> int:
        return sum(map(lambda item: item.quantity, self.item_set.all()))

    @property
    def total(self) -> Decimal:
        return sum(map(lambda item: item.total, self.item_set.all()))

    @property
    def items(self) -> models.QuerySet:
        return self.item_set.all()

    def add(self, product: Product, quantity: int) -> Item:
        return self.item_set.create(product=product, quantity=quantity)
    
    def remove(self, id: int) -> Tuple[int, Dict[str, int]]:
        return self.item_set.filter(pk=id).delete()
    
    def update(self, id: int, quantity: int) -> int:
        if quantity < 1:
            raise ValueError('Please enter a quantity greater than or equal to 1.')
        return self.item_set.filter(pk=id).update(quantity=quantity)
    
    def __str__(self):
        return f'{self.user}: {self.count}'

class Item(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()

    @property
    def total(self) -> Decimal:
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'{self.product}: {self.quantity}'
