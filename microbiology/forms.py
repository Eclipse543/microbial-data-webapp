from django import forms
from django.forms import inlineformset_factory
from .models import CultureResult, AntibioticSusceptibility


class CultureResultForm(forms.ModelForm):

    class Meta:
        model = CultureResult

        fields = [
            'sample_id',
            'patient_id',
            'patient_name',
            'patient_age',
            'patient_sex',
            'specimen',
            'culture_result',
            'organism',
            'collection_date',
        ]

        widgets = {
            'patient_sex': forms.Select(),
            'culture_result': forms.Select(),
            'collection_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class AntibioticSusceptibilityForm(forms.ModelForm):

    class Meta:
        model = AntibioticSusceptibility

        fields = [
            'antibiotic',
            'susceptibility',
        ]

        widgets = {
            'antibiotic': forms.Select(),
            'susceptibility': forms.Select(),
        }


AntibioticFormSet = inlineformset_factory(
    CultureResult,
    AntibioticSusceptibility,
    form=AntibioticSusceptibilityForm,
    extra=1,
    can_delete=True
)
