from django.forms import ModelForm
from .models import food, order

class ordersForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'