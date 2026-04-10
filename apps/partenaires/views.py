from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Partenaire
from .Serializers import PartenaireSerializer

class PartenaireListView(generics.ListAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer