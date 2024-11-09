from django import forms
from .models import ClientMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import PasswordResetView, PasswordResetConfirmView


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


class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', 
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter your username',
    }))
    email = forms.EmailField(
        label= 'Email Address',
        widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your email',
    }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Create a password',
    }))
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter password',
    }))
    
    terms = forms.BooleanField(
        required = True,
        error_messages={'required': 'You must agree to the terms and conditions.'},
        widget=forms.CheckboxInput(attrs={
            'class':'form-check-input',
        })        
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'terms')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user
    

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your username',
        }))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }))
    

class CustomPasswordResetView(PasswordResetView):
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput
    )