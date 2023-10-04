from django.shortcuts import render, get_object_or_404
from django.views import generic
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

def part_service_description(request, pk):
    return render(
        request, 'library/part_service_description.html',
        {'part_service' : get_object_or_404(models.PartService.objects.all(), pk=pk)}
    )

class CarModelView(generic.DetailView):
    model = models.CarModel
    template_name = 'library/car_model.html'