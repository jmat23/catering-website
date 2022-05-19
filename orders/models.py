from django.db import models

# Create your models here.
class food(models.Model):
    food_name = models.CharField(max_length = 100)
    s_stock = models.IntegerField()
    m_stock = models.IntegerField()
    l_stock = models.IntegerField()

    def __str__(self):
        return self.food_name

class orders(models.Model):
    name = models.CharField(max_length = 100)
    cash = models.BooleanField(default = True)
    delivery = models.BooleanField(default = False)
    contact = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    postcode = models.CharField(max_length = 4)
    foods = models.ForeignKey(food, null=True, on_delete=models.SET_NULL)
    total_amount = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return str(self.id)