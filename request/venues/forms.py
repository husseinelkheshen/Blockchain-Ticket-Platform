from django import forms
from datetime import datetime

class ValidateTicketForm(forms.Form):
    ticket_num = forms.IntegerField()
    user_email = forms.CharField(max_length=100)
    hsh = forms.CharField(max_length=5, help_text="Enter last 5 characters of hash.")


class ScheduleReleaseForm(forms.Form):
    scheduled_for = forms.DateField(initial=datetime.now())
    section = forms.CharField(max_length=100)