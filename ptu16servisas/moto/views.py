from typing import Any
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpRequest, HttpResponse
from . import models, forms

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

class PartServiceDetailView(generic.edit.FormMixin, generic.DetailView):
    model = models.PartService
    template_name = 'library/part_service_description.html'
    form_class = forms.PartServiceForm

def get_initial(self) -> dict[str, Any]:
    initial = super().get_initial()
    initial['service'] = self.kwargs['pk']
    initial['reviewer'] = self.request.user
    return initial

def post(self, *args, **kwargs) -> HttpResponse:
    self.object = self.get_object()
    form = self.get_form()
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)

def form_valid(self, form) -> HttpResponse:
    form.instance.service = self.object
    form.instance.reviewer = self.request.user
    form.save()
    return super().form_valid(form)

def get_success_url(self):
    return reverse('part_service_description', kwargs={'pk': self.object.pk})
    

def part_service_description(request, pk):
    return render(
        request, 'library/part_service_description.html',
        {'part_service' : get_object_or_404(models.PartService.objects.all(), pk=pk)}
    )

class CarModelView(generic.DetailView):
    model = models.CarModel
    template_name = 'library/car_model.html'


class OrderLineView(generic.DetailView):
    model = models.OrderLine
    template_name = 'library/order_line.html'

def order_line(request):
    return render(
        request, 'library/order_line.html',
        {'order_line_list1' : models.OrderLine.objects.all()}
    )