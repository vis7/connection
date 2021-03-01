from django import forms

from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = [
            'event_name',
            'description',
            'location',
            'datetime',
            'event_type',
        ]
        widgets = {
            'datetime': DateInput()
        }



