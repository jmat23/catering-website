from django.forms import ModelForm
from django import forms
from .models import food, order, order_item, food_product

class ordersForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class orderAddItem(ModelForm):
    class Meta:
        model = order_item
        fields = '__all__'    