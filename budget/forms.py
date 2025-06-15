from django import forms
from .models import Entry
from captcha.fields import CaptchaField

class EntryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Entry
        fields = ['type', 'amount', 'category', 'date', 'description', 'receipt']  
        labels = {
            'type': 'Typ',
            'amount': 'Kwota',
            'category': 'Kategoria',
            'date': 'Data',
            'description': 'Opis',
            'receipt': 'Paragon (plik)', 
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
