from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.TextField(blank=False, null=False)
    group_id = models.ForeignKey(
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