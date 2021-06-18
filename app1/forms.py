from django import forms
from .models import Employees
class UserForm(forms.ModelForm):
    class Meta:
        model = Employees
        widgets = {
        'password': forms.PasswordInput(),
    }