from django.shortcuts import render

# Create your views here.
def tests(request):
	return render(request, 'equipment.html')
