from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import food, food_product, order_item
from .forms import ordersForm, orderAddItem

# Create your views here.
def tests(request):
	menu = food.objects.all()
	return render(request, 'orders.html', {'menu': menu})

def createOrder(request):
	menu = food_product.objects.all()
	form1 = ordersForm()
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		form1 = ordersForm(request.POST)
		if form1.is_valid():
			neworder = form1.save()
		
		for items in menu:
			# if request.POST.get(items.name) != 0:
			order_item.objects.create(parent_order = neworder, product = items, quantity = request.POST.getlist(items.name)[0])
		if form1.is_valid():
			# form1.save()
			return redirect('/')
	
	context = {'form1': form1, 'menu': menu}
	return render(request, 'menu_form.html', context)