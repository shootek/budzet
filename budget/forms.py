from django import forms
from .models import Entry
from captcha.fields import CaptchaField

class EntryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Entry
        fields = ['type', 'amount', 'category', 'date', 'description', 'captcha']
        labels = {
            'type': 'Typ',
            'amount': 'Kwota',
            'category': 'Kategoria',
            'date': 'Data',
            'description': 'Opis',
            'captcha': 'Zabezpieczenie (Captcha)',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
