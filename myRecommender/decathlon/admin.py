from django.contrib import admin
from . import models



# Register your models here.
class Cycle(admin.ModelAdmin):
	fields = (
			  'gender',
			  'cycle_type',
			  'cycling_Reason',
			  'cycling_id',
			  'mrp',
			  'age')

admin.site.register(models.Cycle,  Cycle)
