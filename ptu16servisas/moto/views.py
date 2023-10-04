from django.shortcuts import render
from . import models

def index(request):
    context = {
        'cars': models.CarModel.objects.all(),
        'customers': models.Customer.objects.all(),
        'orders': models.OrderLine.objects.filter(status=2).count,
        'services': models.PartService.objects.all(),
    }
    return render(request, 'library/index.html', context)

def model(request):
    return render(
                request,
                'library/models.html', 
                {'models_list' :models.CarModel.objects.all()}
                )

def services(request):
    return render(
                request, 
                'library/services.html', 
                {'services_list' : models.PartService.objects.all()}
                )