from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField( max_length=50, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class SubscriptionForm(forms.ModelForm):
    password2 = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        ordering = ['username']


    
    
    
