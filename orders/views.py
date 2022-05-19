from django.shortcuts import render
from django.http import HttpResponse
from .models import food

# Create your views here.
def tests(request):
	menu = food.objects.all()
	return render(request, 'orders.html', {'menu': menu})
