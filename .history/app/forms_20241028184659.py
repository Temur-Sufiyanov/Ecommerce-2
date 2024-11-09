from django import forms
from .models import 


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput())