from django import forms
from .models import ClientMessage


class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.HiddenInput())
    

class ClientMessageForm(forms.ModelForm):
    class Meta:
        model = ClientMessage
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message here...',
                'rows': 4
            }),
        }   