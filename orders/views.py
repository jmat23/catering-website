from django.shortcuts import render
from django.http import HttpResponse
from orders.testmenu import generate

# Create your views here.
def tests(request):
	menu = generate()
	return render(request, 'orders.html', {'menu': menu})
