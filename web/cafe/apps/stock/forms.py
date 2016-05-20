from django.forms import ModelForm, ModelChoiceField
from .models import ProductGroup, Product

class ProductGroupForm(ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['group', 'name', 'price', 'price_rent', 'price_other', 'stock']

    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', None)
        super(ProductForm, self).__init__(*args, **kwargs)

        if groups:
            self.fields['group'] = ModelChoiceField(queryset=groups, empty_label='Choose a product group')