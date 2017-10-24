from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#from .models import Choice, Question


class IndexView(generic.ListView):
    pass
