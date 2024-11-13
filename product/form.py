
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','discount_price','net_weight','storage_method','discount_percentage','image']









