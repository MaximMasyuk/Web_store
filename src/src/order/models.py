from django.db import models
from card.models import Card
# Create your models here.

class Order(models.Model):
    card = models.ForeignKey(
        Card,
        verbose_name="Корзина",
        related_name="book",
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    address = models.TextField("Адресс доставки")
    created = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    status = models.BooleanField("Выполнен", default= False)

    def get_absolute_url(self):
        return f"/book/list/"