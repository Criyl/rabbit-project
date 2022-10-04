from email.policy import default
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from core.tasks import calculate_fibonacci, calculate_factorial, celery_sleep


class FibForm(forms.Form):

    number = forms.IntegerField(
        min_value=1,
        initial=1
    )

    multiple = forms.IntegerField(
        min_value=1,
        initial=1
    )

    queue = forms.ChoiceField(
        choices=(
            ("default", "default"),
            ("special", "special"),
        )
    )

    method = forms.ChoiceField(
        choices=(
            ("fib", "Fibonacci"),
            ("fact", "Factorial"),
            ("sleep", "Sleep")
        )
    )