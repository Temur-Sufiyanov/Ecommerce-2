from django import forms

class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices = []
    )