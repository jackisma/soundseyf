from django import forms 
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import Contact 



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact 
        fields = '__all__'

