from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class FibForm(forms.Form):
    num = forms.IntegerField(
        min_value=1,
    )
