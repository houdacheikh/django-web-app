from dataclasses import fields
from django import forms
from listings.models import Band,Annonce
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000);
class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     exclude = ('active', 'official_homepage')
class AnnForm(forms.ModelForm):
   class Meta:
     model = Annonce
     fields = '__all__'   