from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _
from cafe.utils.fields import JSONField

class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    group = models.ForeignKey(
        'ProductGroup',
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.IntegerField()
    price_rent = models.IntegerField()
    price_other = JSONField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['pk']
        permissions = (
            ("rent_out_product", "Can rent out a product"),
        )

    def validate_unique(self, exclude=None):
        if Product.objects.filter(name=self.name).exists():
            raise ValidationError({'name': ValidationError(_('Product name already exists.'))}, code='invalid')

class ProductGroup(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['pk']

    def validate_unique(self, exclude=None):
        if ProductGroup.objects.filter(name=self.name).exists():
            raise ValidationError({'name': ValidationError(_('Group name already exists.'))}, code='invalid')

    def __str__(self):
        return self.name

class StockCount(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    price_type = models.CharField(blank=False, null=True, max_length=256)
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
    name = models.CharField(blank=False, null=False, max_length=256)
    price = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        ordering = ['pk']
