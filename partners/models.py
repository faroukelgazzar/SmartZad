from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class partnerbasic(models.Model):
    PS_Name = models.CharField(max_length=255)
    PS_Mail = models.EmailField(max_length=254, unique=True)
    PS_DB = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author_Mail = models.EmailField(max_length=254, unique=False)

    def __str__(self):
        return self.PS_Name