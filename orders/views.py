from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import food
from .forms import ordersForm

# Create your views here.
def tests(request):
	menu = food.objects.all()
	return render(request, 'orders.html', {'menu': menu})

def createOrder(request):
	form = ordersForm()
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		form = ordersForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context = {'form': form}
	return render(request, 'menu_form.html', context)