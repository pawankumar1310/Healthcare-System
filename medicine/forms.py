from django import forms
from django.db.models import fields
from .models import Medicine 


class MedicineForm(forms.ModelForm):
	class Meta:
		model = Medicine
		fields = ['name_medicine','manufactured_by','substitute','price_medicine','use_medicine','benefits_medicine',
		'side_effects_medicine','safety_advice_medicine','picture']
		widgets = {
		'manufactured_by': forms.Select(attrs={'class': 'form-control'}),
		'name_medicine': forms.TextInput(attrs={'class': 'form-control'}),
		'price_medicine': forms.NumberInput(attrs={'class': 'form-control'}),
		'use_medicine': forms.TextInput(attrs={'class': 'form-control'}),
		'benefits_medicine': forms.TextInput(attrs={'class': 'form-control'}),
		'side_effects_medicine': forms.TextInput(attrs={'class': 'form-control'}),
		'safety_advice_medicine': forms.TextInput(attrs={'class': 'form-control'}),
		}


