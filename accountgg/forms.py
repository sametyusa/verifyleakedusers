from django import forms
from django.forms import TextInput, PasswordInput
class FileForm(forms.Form):  
    file = forms.FileField() # for creating file input  

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=254,
        )
    password=forms.CharField(
        max_length=254,
        widget=forms.PasswordInput()
        )