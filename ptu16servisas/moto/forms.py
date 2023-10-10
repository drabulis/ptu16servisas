from django import forms
from . import models

class PartServiceForm(forms.ModelForm):
    class Meta:
        model = models.PartService
        fields = '__all__'
        widgets = {
            'service' : forms.HiddenInput(),
            'reviewer' : forms.HiddenInput(),
        }