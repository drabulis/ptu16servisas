from django.contrib import admin
from . import models

admin.site.register(models.PartService)
admin.site.register(models.CarModel)
admin.site.register(models.Customer)
admin.site.register(models.OrderLine)
admin.site.register(models.ServiceOrder)

@admin.register(models.PartServiceReview)
class PartServiceReviewAdmin(admin.ModelAdmin):
    list_display = ('service', 'reviewer', 'created_at')
    list_display_links = ('created_at',)

