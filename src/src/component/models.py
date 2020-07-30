from django.db import models
from component_option.models import Categorie ,ManufacturingFirm
# Create your models here.

class Component (models.Model):

    name = models.CharField (max_length= 50)

    image = models.ImageField(upload_to='user_flowers', null= True)

    categorie = models.ForeignKey(
        Categorie,
        related_name="Categorie",
        on_delete=models.PROTECT
    )

    manufacturing_firm = models.ForeignKey(
        ManufacturingFirm,
        related_name="Manufacturing_firm",
        on_delete=models.PROTECT
    )


    description = models.TextField()

    price = models.IntegerField()


    year_of_publishing = models.DateField()

    in_stock = models.IntegerField()

    rating = models.FloatField()

    created = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False)