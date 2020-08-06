from django import forms
"""
class ContactForm(forms.Form):
    sujet = forms.CharField( max_length=100, required=False)
    message = forms.CharField( required=True, widget=forms.Textarea)
    envoyeur = forms.EmailField(label = "Votre adresse e-mail")
    renvoi = forms.BooleanField(required=False, help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé")

    def clean_message(self):
        message = self.cleaned_data['message']
        if  "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
        
        return message

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message: # Est-ce que sujet et message sont valides ?
            if "pizza" in message and "pizza" in message:
                raise self.add_error('message', "On ne veut pas entendre parler de pizza !")

        return cleaned_data
"""
class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()

