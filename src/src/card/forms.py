from django.forms import ModelForm
from .models import ComponentInCard


class ComponentInCardForm(ModelForm):
    class Meta:
        model = ComponentInCard
        fields = ['quantity', ]
