from django.db import models

# Create your models here.
class food(models.Model):
    food_name = models.CharField(max_length = 100)

    Categories = [
        ('CHICKEN', 'Chicken'), 
        ('PORK', 'Pork'), 
        ('BEEF', 'Beef'), 
        ('SEAFOOD', 'Seafood'), 
        ('VEGETABLE', 'Vegetable'), 
        ('PASTA', 'Pasta'), 
        ('SOUP', 'Soup'), 
        ('DESSERT', 'Dessert'), 
    ]

    category = models.CharField(
        max_length = 9,
        choices = Categories,
        default = 'CHICKEN',
    )

    def __str__(self):
        return self.food_name

class order(models.Model):
    name = models.CharField(max_length = 100)
    cash = models.BooleanField(default = True)
    delivery = models.BooleanField(default = False)
    contact = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    postcode = models.CharField(max_length = 4)
    total_amount = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return str(self.id)

class food_product(models.Model):
    parent_food = models.ForeignKey(food, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length = 100)

    Sizes = [
        ('SML', 'Small'),
        ('MED', 'Medium'),
        ('LRG', 'Large'),
    ]

    size = models.CharField(
        max_length = 3,
        choices = Sizes,
        default = 'SML'
    ) 

    stock = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class order_item(models.Model):
    parent_order = models.ForeignKey(order, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(food_product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.parent_order.id)