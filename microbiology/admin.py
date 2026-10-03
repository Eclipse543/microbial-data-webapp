from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CultureResult


@admin.register(CultureResult)
class CultureResultAdmin(admin.ModelAdmin):

    list_display = (
        'sample_id',
        'patient_id',
        'specimen',
        'organism',
        'culture_result',
        'collection_date',
    )

    search_fields = (
        'sample_id',
        'patient_id',
        'organism',
    )

    list_filter = (
        'specimen',
        'culture_result',
        'organism',
    )
