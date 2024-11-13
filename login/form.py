
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomCreationForm(UserCreationForm):
    phone_num = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False, widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(required=False, widget=forms.PasswordInput,label='Confirm Password')


    class Meta:
        model = User
        fields = ('username','phone_num','email','password1','password2')