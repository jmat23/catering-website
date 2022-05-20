from django.contrib import admin
from .models import food
from .models import order, order_item, food_product
# Register your models here.
admin.site.register(food)
admin.site.register(order)
admin.site.register(order_item)
admin.site.register(food_product)