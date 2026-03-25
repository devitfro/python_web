from django import forms
from .models import Event, Participant
from django.forms import formset_factory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']