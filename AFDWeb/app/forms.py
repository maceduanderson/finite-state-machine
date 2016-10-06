"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app import models

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('name', 'finalstate')

class TransitionForm(forms.ModelForm):
    class Meta:
        model = TransitionModel
        fields = ('shortValidationArg', 'nextstate')                