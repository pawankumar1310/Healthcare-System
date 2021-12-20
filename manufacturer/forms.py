from medicine.models import Manufacturer
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm, UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django.forms import widgets


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label_suffix='', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),label_suffix='' ,strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label=_("New Password (Again)"),label_suffix='', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
  }

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name','email','address','contact_no']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'contact_no':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }