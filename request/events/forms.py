from django import forms
from datetime import datetime

from .models import Event

class CreateEventForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, widget=forms.Textarea)
    when = forms.DateTimeField(initial=datetime.now(), required=False)

class CreateTicketsForm(forms.Form):
    section = forms.CharField(max_length=100)
    min_row = forms.IntegerField()
    max_row = forms.IntegerField()
    min_seat= forms.IntegerField()
    max_seat= forms.IntegerField()
    face_value = forms.FloatField()

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "description", "when")

class EditTicketsForm(forms.Form):
    section = forms.CharField(max_length=100)
    row = forms.IntegerField(required=False)
    seat = forms.IntegerField(required=False)
    face_value = forms.FloatField(required=False)