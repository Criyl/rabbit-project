from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from core.forms import FibForm
from core.tasks import calculate_fibonacci
from core.models import Fibonacci


class FibView(FormView):
    template_name = 'fib.html'
    form_class = FibForm

    def form_valid(self, form):
        num = form.cleaned_data.get('num')

        result = calculate_fibonacci.s(num).delay().get()
        calculate_fibonacci.s(num).apply_async()
        print(result)
        Fibonacci.objects.create(index=num, value=result).save()
        return redirect('.')

    def get_context_data(self, **kwargs):
        context = super(FibView, self).get_context_data(**kwargs)
        context['fibs'] = Fibonacci.objects.all()
        return context
