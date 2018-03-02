from django import forms

class ValidateTicketForm(forms.Form):
    ticket_num = forms.IntegerField()

class ScheduleReleaseForm(forms.Form):
    scheduled_for = forms.DateField()