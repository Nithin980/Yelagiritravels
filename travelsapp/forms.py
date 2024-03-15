from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from .models import Booking,Car
from django.contrib.auth import get_user

class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    otp=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Otp'}))
    class Meta:
        model =User
        fields =['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    username =forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password =forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    
    
class PasswordChangeCustomForm(PasswordChangeForm):
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    
class BookForm(forms.ModelForm):

    username=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    Phoneno=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter valid phone number'}))
    boarding=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Boarding Location'}))
    drop=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Drop Location'}))
    date_of_travel = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'Date of travel', 'class': 'form-control'}))
    car=forms.CharField(widget=forms.TextInput())
    status=forms.CharField(widget=forms.HiddenInput(),initial='Booked')
    
    
    
    class Meta:
        model = Booking
        fields=['username','email','Phoneno','boarding','drop','status','date_of_travel','car']
        
class verifyotp(UserCreationForm):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    otp=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Otp'}))
