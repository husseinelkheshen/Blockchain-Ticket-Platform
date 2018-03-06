from django import forms

class ValidateTicketForm(forms.Form):
    ticket_num = forms.IntegerField()
    user_email = forms.CharField(max_length=100)
    hsh = forms.CharField(max_length=5)


class ScheduleReleaseForm(forms.Form):
    scheduled_for = forms.DateField()
    section = forms.CharField(max_length=100)