from django import forms

USER_TYPE_CHOICES = (
    ("customer", "Customer"),
    ("venue", "Venue")
)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
