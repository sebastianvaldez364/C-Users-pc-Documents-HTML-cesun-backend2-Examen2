from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto

        fields = ['marca', 'modelo', 'año', 'precio']

        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la marca'
            }),

            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el modelo'
            }),

            'año': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el año'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
        }