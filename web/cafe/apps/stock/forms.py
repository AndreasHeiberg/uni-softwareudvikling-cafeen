from django.forms import ModelForm
from .models import ProductGroup

class ProductGroupForm(ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['name']