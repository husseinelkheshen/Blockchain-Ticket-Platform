from django import forms

USER_TYPE_CHOICES = (
    ("customer", "Customer"),
    ("venue", "Venue")
)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    name = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
