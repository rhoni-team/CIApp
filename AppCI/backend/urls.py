""" URL configuration for backend app """

from django.urls import path
from backend.views.disease_view import DiseasesListView

urlpatterns = [
    path('diseases', DiseasesListView.as_view(), name="diseases_names"),
]
