from material import *
from django import forms
from . import models


class CycleForm(forms.ModelForm):

    class Meta:
        model = models.Cycle
        fields = (
                  'gender',
                  'cycle_type',
                  'cycling_Reason',
                  'cycling_id',
                  'mrp',
                  'age')