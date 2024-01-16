from django import forms
from django.forms.models import BaseModelFormSet

from .models import Product, Production


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['image']

class DateInput(forms.DateInput):
    input_type = 'date'

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }

class BaseProductionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseProductionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Production.objects.none()
