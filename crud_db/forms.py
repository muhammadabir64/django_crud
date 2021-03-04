from django import forms
from .models import User_Info

class UserForm(forms.ModelForm):
    class Meta:
        model = User_Info
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }