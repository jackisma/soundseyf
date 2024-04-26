from django import forms 
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import *



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact 
        fields = '__all__'



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'