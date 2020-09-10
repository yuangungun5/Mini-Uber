from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'is_driver', 'licence', 'car_id', 'level', 'max_passenger', 'special']
        
class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'licence', 'car_id', 'level', 'max_passenger', 'special']
        
'''
class DriverRegisterForm(forms.modelForm):
    name = models.CharField(max_length=30, default='')
    licence = models.CharField(max_length=12,default='000000000000')
    car_id = models.CharField(max_length=10,default='CDC-000000')
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='S')
'''
