from django.shortcuts import render
from django.db import models
from json_demo.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.core import serializers

# Create your views here.

from .forms import UserModelForm


def userDetails(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            users = UserDetails.objects.all()
            users = serializers.serialize('json', users, indent = 4)
            for item in users:
                return HttpResponse(users, content_type="application/json")


            #return render(request, 'display.html', {'users': users})



    else:
        form_class = UserModelForm

    return render(request, 'userdetails.html', {
        'form': form_class,
    })