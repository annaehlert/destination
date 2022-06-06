from django import forms
from .models import Client
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone
from django.core.exceptions import ValidationError


class AddClientForm(forms.Form):
    name = forms.CharField(label="Imię", max_length=40)
    surname = forms.CharField(label="Nazwisko", max_length=100)


# Validation method for dates, not to be from the past
def validate_date(value):
    if value < timezone.now():
        raise ValidationError(
            "Nie można wybrać daty z przeszłości.")


# Form for addings orders with DateTimePicker input
class AddDestinationForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Klient', required=True)
    address = forms.CharField(label="Adres", max_length=200, required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'ul. Testowa 1/1, 00-000 Warszawa'}))
    order_date = forms.DateTimeField(
        label="Data zamówienia",
        required=True,
        widget=DateTimePickerInput(attrs={'class': 'datepicker'}),
        validators=[validate_date]
    )
