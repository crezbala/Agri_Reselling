from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import prof
from django.contrib.auth.models import User
        
class DesignerProfilesForm(forms.ModelForm):
    class Meta:
        # image = forms.ImageField()
        model = prof
        fields = '__all__'
        #fields=['user', 'name', 'phn', 'address', 'email', 'education', 'country', 'state', 'profile_pic']
        # exclude = ['user']    