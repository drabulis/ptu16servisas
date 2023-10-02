from django.shortcuts import render
from . import models

def index(request):
    context = {
        'cars': models.CarModel.objects.all(),
        'customers': models.Customer.objects.all(),
        'orders': models.OrderLine.objects.filter(status=3).count,
        'services': models.PartService.objects.all(),
    }
    return render(request, 'library/index.html', context)
