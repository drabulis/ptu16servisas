from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', include ('user_profile.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('services/', views.services, name='services'),
    path('models/', views.model, name='models'),
    path('part_service_description/<int:pk>/', views.part_service_description, name='part_service_description'),
    path('car_model/<int:pk>/', views.CarModelView.as_view(), name='car_model'),
    #path('order_line/<int:pk>/', views.OrderLineView.as_view(), name='order_line'),
    path('order_line/', views.order_line, name='order_line'),
]