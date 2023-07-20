from django.shortcuts import render
# Create your views here.


def new_partner(request):
    return render(request, 'partners/createpartner.html')
