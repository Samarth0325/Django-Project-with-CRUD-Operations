from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm): #It is a form we create for a user.
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),#we use form-control to convert normal form into bootstrap form
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs= {'class':'form-control'})
            ,
        }