from django.shortcuts import render

from .forms import CycleForm
from .final_recommend import cycle_recommend

from django.urls import reverse_lazy
from django.views import generic


class Dashboard(generic.TemplateView):
    template_name = 'decathlon/base.html'


def get_name(request):
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            form_data = {'Gender': form.cleaned_data['gender'],
                         'Age': form.cleaned_data['age'],
                         'Cycle_Type': form.cleaned_data['cycle_type'],
                         'Cycle_id': form.cleaned_data['cycling_id'],
                         'Cycling_Reason': form.cleaned_data['cycling_Reason'],
                         'MRP': form.cleaned_data['mrp'],
                         }
            return render(request,
                          'decathlon/data.html',
                          {'data': cycle_recommend(form_data)})

    else:
        form = CycleForm()

    return render(request, 'decathlon/name.html', {'form': form})


def get_data(request):
    return render(request,
                  'decathlon/data.html',
                  {'data': cycle_recommend()})
