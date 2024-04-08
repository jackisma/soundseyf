from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# over writing the django user creation form for signing up users and adding email field
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
            