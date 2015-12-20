from django import forms
from captcha.fields import CaptchaField
from gics.models import Contact


class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='Entrez le code')

    class Meta:
        model = Contact
        fields = ['action', 'name', 'email', 'message']
