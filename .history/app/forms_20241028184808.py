from django import forms
from .models import ClientMessage


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput())
    

class ClientMessageForm(forms.ModelForm):
    class Meta:
        model =     