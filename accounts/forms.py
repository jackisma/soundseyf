from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Over Writing Django's User Creation Form for adding Email field
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label='email') 
    class Meta:
        model = User 
        fields = ("username","email","password1","password2")
        def save(self , commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
                return user 
            