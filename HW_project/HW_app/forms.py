from django import forms

from .models import Order, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        
# class ProductForm(forms.ModelForm):
#     image = forms.ImageField()