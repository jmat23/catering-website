from django.contrib import admin
from .models import food
from .models import orders
# Register your models here.
admin.site.register(food)
admin.site.register(orders)