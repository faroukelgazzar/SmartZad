from django import forms
from django.contrib.auth.models import User
from .models import partnerbasic
# creating a form


class NewPartnerForm(forms.ModelForm):
    class Meta:
        model = partnerbasic
        fields = ('PS_Name', 'PS_Mail',
                  'PS_DB', 'author_Mail')
