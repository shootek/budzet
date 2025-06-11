from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['type', 'amount', 'category', 'date', 'description']
        labels = {
            'type': ('Typ'),
            'amount': ('Kwota'),
            'category': ('Kategoria'),
            'date': ('Data'),
            'description': ('Opis'),
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
