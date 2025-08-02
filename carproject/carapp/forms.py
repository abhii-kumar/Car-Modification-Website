from django import forms 
from carapp.models import *
class contactform(forms.ModelForm):
     class Meta:
         model=contact
         fields="__all__"     
 
class apponmentform(forms.ModelForm):
    class Meta:
        model=apponment
        fields="__all__"     
