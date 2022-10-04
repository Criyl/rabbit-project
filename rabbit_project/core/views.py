from django.views.generic.edit import FormView
from django.shortcuts import redirect

from core.forms import FibForm
from core.tasks import calculate_fibonacci, calculate_factorial, celery_sleep
from core.models import ResultRecord


class FibView(FormView):
    template_name = 'fib.html'
    form_class = FibForm

    def form_valid(self, form):
        number = form.cleaned_data.get('number')
        task_queue = form.cleaned_data.get('queue')
        task_method = form.cleaned_data.get('method')
        multiple = form.cleaned_data.get('multiple')

        func = calculate_fibonacci
        if task_method == "fib":
            func = calculate_fibonacci
        elif task_method == "fact":
            func = calculate_factorial
        elif task_method == "sleep":
            func = celery_sleep

        async_results = []
        for i in range(multiple):
            async_results += [func.s(number).apply_async(queue=task_queue)]
        for i in range(multiple):
            ResultRecord.objects.create(
                    index=number,
                    method=task_method,
                    value=async_results[i].get()
                ).save()
            redirect('.')

        return redirect('.')

    def get_context_data(self, **kwargs):
        context = super(FibView, self).get_context_data(**kwargs)
        context['results'] = ResultRecord.objects.all()
        return context
