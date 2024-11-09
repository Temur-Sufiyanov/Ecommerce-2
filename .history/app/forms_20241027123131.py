from django import forms
from .models import Product

class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices = [(i, str(i)) for i in range(1,6)],
        widget= forms.RadioSelect,
        label = 'Rate this product'
    )
    
    class Meta:
        model 