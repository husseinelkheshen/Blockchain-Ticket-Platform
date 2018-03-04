from django import forms
from datetime import datetime

class CreateEventForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    when = forms.DateTimeField(initial=datetime.now(), required=False)

class CreateTicketsForm(forms.Form):
    section = forms.CharField(max_length=100)
    min_row = forms.IntegerField()
    max_row = forms.IntegerField()
    min_seat= forms.IntegerField()
    max_seat= forms.IntegerField()
    face_value = forms.FloatField()