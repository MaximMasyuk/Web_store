from django.forms import ModelForm
from .models import Component

class ComponentCreateForm(ModelForm):
    class Meta:
        model = Component
        fields = [
            'name',
            'categorie',
            'manufacturing_firm',
            'description',
            'price',
            'year_of_publishing',
            'in_stock',
            'rating',
        ]   