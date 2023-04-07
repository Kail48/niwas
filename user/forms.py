from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class PhoneForm(forms.Form):
    number = PhoneNumberField(region="NP")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']
        labels = {
        "username":  "Username",
        "email": "Email",
        "password1": "Password",
        "password2":"Confirm password"
    }
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username','email']