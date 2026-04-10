from django.urls import path
from .views import RealisationListView

urlpatterns = [
    path('', RealisationListView.as_view(), name='realisations'),
]