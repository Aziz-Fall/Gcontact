from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-group'
        }
    ))
    last_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-group'
        }
    ))
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-group'
        }
    ))
    #email.widget.attrs.update({'class': 'form-group'})