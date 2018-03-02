from django import forms

class CreateEventForm(forms.Form):
    name = forms.CharField(max_length=100)

class CreateTicketsForm(forms.Form):
    section = forms.CharField(max_length=100)
    min_row = forms.CharField(max_length=100)
    max_row = forms.CharField(max_length=100)
