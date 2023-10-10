from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model

STATUS_CHOICES = [
    (0, "Reserved"),
    (1, "Working"),
    (2, "Done"),
    (3, "Canceled"),
]

User = get_user_model()

class PartService(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    price = models.IntegerField()
    description = models.TextField(_("Description"), blank=True, max_length=1000)
    

    class Meta:
        verbose_name = _("PartService")
        verbose_name_plural = _("PartServices")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("PartService_detail", kwargs={"pk": self.pk})


class CarModel(models.Model):
    make = models.CharField(_("Make"), max_length=50)
    model = models.CharField(_("Model"), max_length=50)
    year = models.IntegerField()

    class Meta:
        verbose_name = _("CarModel")
        verbose_name_plural = _("CarModels")

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def get_absolute_url(self):
        return reverse("CarModel_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    name = models.CharField(_("Name"), max_length=100, db_index=True)
    car_model_id = models.ForeignKey(CarModel,
                                    verbose_name=_("Car"),
                                    on_delete=models.CASCADE,
                                    related_name="customers",
                                    db_index=True
                                    )
    plate = models.CharField(_("Plate"), max_length=10, db_index=True)
    vin = models.CharField(_("VIN"), max_length=17)
    color = models.CharField(_("Color"), max_length=50)

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def __str__(self):
        return f"{self.car_model_id} {self.plate} {self.color}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class ServiceOrder(models.Model):
    customer_id = models.ForeignKey(Customer,
                                    verbose_name=_("Customer"),
                                    related_name="service_orders",
                                    on_delete=models.CASCADE,
                                    db_index=True,
                                    )
    date = models.DateField()

    class Meta:
        verbose_name = _("ServiceOrder")
        verbose_name_plural = _("ServiceOrders")
        ordering = ["customer_id",]

    def __str__(self):
        return f"{self.customer_id} {self.date}"

    def get_absolute_url(self):
        return reverse("ServiceOrder_detail", kwargs={"pk": self.pk})


class OrderLine(models.Model):
    part_service_id = models.ForeignKey(PartService,
                                        verbose_name=_("Service"),
                                        on_delete=models.CASCADE,
                                        related_name="order_lines",
                                        db_index=True
                                        )
    order_id = models.ForeignKey(ServiceOrder, 
                                 verbose_name=_("Customer"), 
                                 on_delete=models.CASCADE,
                                 related_name="order_lines",
                                 db_index=True
                                 )
    quantinity = models.IntegerField()
    price = models.IntegerField()
    status = models.PositiveSmallIntegerField(_("Status"), choices=STATUS_CHOICES, default=0, db_index=True)
    customer = models.ForeignKey(User,
                                verbose_name=_(""),
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                )

    class Meta:
        verbose_name = _("OrderLine")
        verbose_name_plural = _("OrderLines")
        ordering = ["order_id", "part_service_id", "status"]

    def __str__(self):
        return f"{self.order_id} {self.part_service_id} {self.quantinity} {self.price} {self.status}"

    def get_absolute_url(self):
        return reverse("OrderLine_detail", kwargs={"pk": self.pk})

    @property
    def total_price(self):
        return self.quantinity * self.price

class PartServiceReview(models.Model):
    service = models.ForeignKey(PartService, 
                                verbose_name=_("Service"), 
                                on_delete=models.CASCADE,
                                related_name="review",)
    reviewer = models.ForeignKey(User, 
                                 verbose_name=_("Reviewer"), 
                                 on_delete=models.CASCADE,
                                 related_name="service_review",)
    content = models.TextField(_("Content"), max_length=4000)
    created_at = models.DateTimeField(_("Created at"), 
                                      auto_now_add=True, 
                                      db_index=True)

    class Meta:
        verbose_name = _("ServiceReview")
        verbose_name_plural = _("ServiceReviews")
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.service} {self.reviewer}"

    def get_absolute_url(self):
        return reverse("PartServiceReview_detail", kwargs={"pk": self.pk})

    
