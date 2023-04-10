from django import forms
from .models import ProductModel, InventoryModel
from django.forms import ModelForm, NumberInput

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'code', 'description', 'price', 't_size', 'quantity']



class InventoryForm(ModelForm):
    class Meta:
        model = InventoryModel
        fields = ['total']
        widgets = {
            'total': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100px;',
                'placeholder': '입고량'
            }),

        }


class InventoryDeleteForm(ModelForm):
    class Meta:
        model = InventoryModel
        fields = ['total']
        widgets = {
            'total': NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100px;',
                'placeholder': '출고량'
            }),

        }
