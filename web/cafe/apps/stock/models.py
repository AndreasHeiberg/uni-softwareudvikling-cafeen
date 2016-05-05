from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.TextField(blank=False, null=False)
    group = models.ForeignKey(
        'ProductGroup',
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.IntegerField()
    price_rent = models.IntegerField()
    stock = models.IntegerField(default=0)
    # TODO: Special prices
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['pk']

class ProductGroup(models.Model):
    name = models.TextField(blank=False, null=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['pk']

class StockCount(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['pk']

class StockCountTransaction(models.Model):
    count = models.ForeignKey(
        'StockCount',
        on_delete=models.CASCADE,
        null=True
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True
    )
    stock = models.IntegerField()

    class Meta:
        ordering = ['pk']
