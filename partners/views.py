from django.contrib import messages
from .forms import NewPartnerForm
from .models import partnerbasic
from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def new_partner(request):
    return render(request, 'partners/createpartner.html')
# Create your views here.


def addnewpartner(request):
    form = forms.NewPartnerForm()
    if request.method == "POST":
        NewPartnerForm = NewPartnerForm(request.POST)
        if NewPartnerForm.is_valid():
            NewPartnerForm.save()
            messages.success(request, ('Your movie was successfully added!'))
        else:
            messages.error(request, 'Error saving form')

        return redirect("partners:new_partner")
    partners_form = NewPartnerForm()
    mpartners = partnerbasic.objects.all()
    return render(request=request, template_name="main/home.html", context={'movie_form': movie_form, 'movies': movies})
