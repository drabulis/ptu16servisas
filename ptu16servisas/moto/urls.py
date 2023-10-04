from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('models/', views.model, name='models'),
    path('part_service_description/<int:pk>/', views.part_service_description, name='part_service_description'),
    path('car_model/<int:pk>/', views.CarModelView.as_view(), name='car_model'),
]