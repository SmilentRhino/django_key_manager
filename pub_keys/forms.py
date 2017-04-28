from django import forms
from django.contrib import admin
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet
from pub_keys.models import PublicKey


class PublicKeyForm(forms.ModelForm):
    class Meta:
        model = PublicKey
        fields = ('key_owner', 'pub_key', 'fingerprint')
        widgets = {
            'pub_key': forms.Textarea(),
        }

#class PublicKeyInlineFormSet(BaseInlineFormset):
    
