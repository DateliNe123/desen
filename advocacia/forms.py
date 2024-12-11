from django import forms
from .models import Advogado, Caso

class AdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = '__all__'

class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = '__all__'
