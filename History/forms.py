from lib2to3.pgen2.token import LESS
from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError


class logPage(ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']

    def clean(self):

        cleaned_data = super().clean()
        N = cleaned_data.get('name')
        E = cleaned_data.get('email')
        P = cleaned_data.get('password')
        # pas = cleaned_data.get('password')
        # cpas = cleaned_data.get('cPassword')
        return self.cleaned_data

class changepassword(forms.ModelForm):

    
    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'reenter_password']

    def clean(self):
        cleaned_data = super().clean()

        oldP = cleaned_data.get('old_password')

        newP=cleaned_data.get('new_password')
        reenter_password=cleaned_data.get('reenter_password')
          
        
        
            
            
        return self.cleaned_data 

  

   