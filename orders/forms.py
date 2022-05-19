from django.forms import ModelForm
from .models import food, orders

class ordersForm(ModelForm):
    class Meta:
        model = orders
        fields = '__all__'