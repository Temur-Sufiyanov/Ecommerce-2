from django import forms
from 


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput())