from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm 



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput )
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta :        # Meta :   model ke behaviour ko change kr sakte h  like apne according field  le sakte h 
        model = User 
        fields = ['username', 'email', 'password']


    def clean(self):
        cleaned_data = super().clean()
        password =cleaned_data.get("password")
        confirm_password= cleaned_data.get("confirm_password")


        if(password != confirm_password):
            raise forms.validation

class loginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
