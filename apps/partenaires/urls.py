from django.urls import path
from .views import PartenaireListView

urlpatterns = [
    path('partenaires/', PartenaireListView.as_view(), name='partenaires-list'),
]