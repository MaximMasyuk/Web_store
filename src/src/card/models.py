from django.db import models
from django.contrib.auth import get_user_model
from component.models import Component

# Create your models here.


User = get_user_model()
class Card(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Клиент",
        related_name="cards",
        on_delete=models.PROTECT
    )
    def total_price(self):
        components = self.components.all()
        total = 0
        for component in components:
            total += component.price
        return total


class ComponentInCard(models.Model):
    component = models.ForeignKey(
        Component,
        verbose_name="Книга",
        related_name="components",
        on_delete=models.PROTECT
    )
    card = models.ForeignKey(
        Card,
        verbose_name="Корзина",
        related_name="components",
        on_delete=models.PROTECT
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name="Количество",
        default=1,
        null=False
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.component.name} * {self.quantity}"