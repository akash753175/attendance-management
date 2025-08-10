from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    firstname=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))
    contact_number=forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['firstname', 'username', 'password', 'confirm_password', 'date_of_birth',  'contact_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match !")
        return cleaned_data