from django import forms
from .models import TutorSchedule


class BookingForm(forms.ModelForm):
    class Meta:
        model = TutorSchedule
        fields = ['booked_by', 'booked_email']
