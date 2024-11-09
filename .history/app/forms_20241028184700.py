from django import forms
from .models import C


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput())