from django import forms
from .models import Zakaznik

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Zakaznik
        exclude = ['id']
