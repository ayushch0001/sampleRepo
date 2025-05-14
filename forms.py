from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import make_password


from attandenceDashBoard.models import CustomUserFace ,Attandence, EmployeeRegistration, StoreFaces

class CustomUserForm(UserCreationForm):
    is_superuser = forms.BooleanField(initial=True, widget=forms.HiddenInput(), required=False)
 # Hidden & default True
    class Meta:
        model = CustomUserFace
        fields = ['username', 'first_name', 'last_name', 'password1','password2','is_superuser']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.password =  make_password(user.password)
            if commit:
                user.save()
            return user


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta :
        model = EmployeeRegistration
        fields = ['deprt','name','empId']



class StoreFacesForm(forms.ModelForm):  # Fixed class name
    class Meta:
        model = StoreFaces
        fields = ['front', 'right', 'left', 'emp']
        widgets = {
            'emp': forms.RadioSelect()  # Corrected field widget assignment
        }


