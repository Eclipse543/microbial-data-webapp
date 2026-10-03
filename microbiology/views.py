from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import CultureResult
from .forms import CultureResultForm, AntibioticFormSet


@login_required
def dashboard(request):

    total_samples = CultureResult.objects.count()

    positive_cultures = CultureResult.objects.filter(
        culture_result="Positive"
    ).count()

    negative_cultures = CultureResult.objects.filter(
        culture_result="Negative"
    ).count()

    organism_distribution = (
        CultureResult.objects
        .exclude(organism="")
        .values("organism")
        .annotate(total=Count("organism"))
        .order_by("-total")
    )

    specimen_distribution = (
        CultureResult.objects
        .exclude(specimen="")
        .values("specimen")
        .annotate(total=Count("specimen"))
        .order_by("-total")
    )

    context = {
        "total_samples": total_samples,
        "positive_cultures": positive_cultures,
        "negative_cultures": negative_cultures,
        "organism_distribution": organism_distribution,
        "specimen_distribution": specimen_distribution,
    }

    return render(
        request,
        "microbiology/dashboard.html",
        context
    )


@login_required
@transaction.atomic
def add_culture(request):

    if request.method == "POST":

        form = CultureResultForm(request.POST)

        formset = AntibioticFormSet(
            request.POST,
            prefix="susceptibilities"
        )

        if form.is_valid() and formset.is_valid():

            culture = form.save()

            formset.instance = culture
            formset.save()

            return redirect("culture_list")

    else:

        form = CultureResultForm()

        formset = AntibioticFormSet(
            prefix="susceptibilities"
        )

    context = {
        "form": form,
        "formset": formset,
    }

    return render(
        request,
        "microbiology/add_culture.html",
        context
    )


@login_required
def culture_list(request):

    query = request.GET.get("q", "")

    records = CultureResult.objects.all()

    if query:
        records = records.filter(
            Q(sample_id__icontains=query) |
            Q(patient_id__icontains=query) |
            Q(patient_name__icontains=query) |
            Q(organism__icontains=query) |
            Q(specimen__icontains=query)
        )

    context = {
        "records": records,
        "query": query,
    }

    return render(
        request,
        "microbiology/culture_list.html",
        context
    )


@login_required
@transaction.atomic
def edit_culture(request, id):

    record = get_object_or_404(
        CultureResult,
        id=id
    )

    if request.method == "POST":

        form = CultureResultForm(
            request.POST,
            instance=record
        )

        formset = AntibioticFormSet(
            request.POST,
            instance=record,
            prefix="susceptibilities"
        )

        if form.is_valid() and formset.is_valid():

            form.save()
            formset.save()

            return redirect("culture_list")

    else:

        form = CultureResultForm(
            instance=record
        )

        formset = AntibioticFormSet(
            instance=record,
            prefix="susceptibilities"
        )

    context = {
        "form": form,
        "formset": formset,
        "record": record,
    }

    return render(
        request,
        "microbiology/edit_culture.html",
        context
    )
@login_required
def delete_culture(request, id):

    record = get_object_or_404(
        CultureResult,
        id=id
    )

    if request.method == "POST":

        record.delete()

        return redirect("culture_list")

    return render(
        request,
        "microbiology/delete_culture.html",
        {"record": record}
    )


@login_required
def culture_report(request, id):

    record = get_object_or_404(
        CultureResult,
        id=id
    )

    return render(
        request,
        "microbiology/culture_report.html",
        {"record": record}
    )
