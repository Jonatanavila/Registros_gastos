from django.forms import ModelForm

from .models import Gasto#models


class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion','monto','categoria',]
