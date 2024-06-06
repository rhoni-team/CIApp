""" URL configuration for backend app """

from django.urls import path
from backend.views.disease_view import DiseasesListView, DetailedDisease

urlpatterns = [
    path('diseases', DiseasesListView.as_view(), name="diseases_names"),
    path('diseases/<int:disease_id>', DetailedDisease.as_view(), name="detailed_disease"),
]
