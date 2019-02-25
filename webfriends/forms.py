from django import forms
from registration.forms import RegistrationFormUniqueEmail


class UsuarioFriendsForm(RegistrationFormUniqueEmail):
    nickname = forms.CharField(required=False)
    company = forms.CharField(required=False)

class ContactForm(forms.Form):
    nome = forms.CharField(label="Name")
    email = forms.EmailField(label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    # mensagem = forms.TextField(label="Message")