from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Realisation
from .serializers import RealisationSerializer

class RealisationListView(ListAPIView):
    queryset = Realisation.objects.all().order_by('-id')
    serializer_class = RealisationSerializer

    def get_serializer_context(self):
        return {'request': self.request}