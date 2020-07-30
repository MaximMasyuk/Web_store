from django.forms import ModelForm
from .models import Categorie , ManufacturingFirm

class CategorieCreateForm(ModelForm):
    class Meta:
        model = Categorie
        fields = [
            'name',
            'description'
        ]


class ManufacturingFirmCreateForm(ModelForm):
    class Meta:
        model = ManufacturingFirm
        fields = [
            'name',
        ]