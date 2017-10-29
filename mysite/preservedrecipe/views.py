from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework import viewsets
from .serializers import ClassificationSerializer, IngredientMasterSerializer

from .models import Classification, IngredientMaster


class IndexView(generic.ListView):
    pass


class ClassificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class IngredientMasterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = IngredientMaster.objects.all()
    serializer_class = IngredientMasterSerializer
