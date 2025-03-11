from django import forms
from .models import AvailableSlot

class BookingForm(forms.ModelForm):
    class Meta:
        model = AvailableSlot
        fields = ['date', 'time']