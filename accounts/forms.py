from django import forms
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['user','following','followers','phone']

        widgets = {
            'bday' : forms.DateInput(attrs={'type':'date'})
        }