from django import forms
from .models import ClientMessage
from django.contrib.auth.forms import UserCreationForm


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
        
        def clean_phone_number(self):
            phone = self.cleaned_data.get('phone_number')
            
            if not phone:
                return phone
            return phone.as_international
        