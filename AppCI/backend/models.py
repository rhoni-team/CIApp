"""Models for backend app"""
from django.db import models


class IsolationType(models.Model):
    """Model for 'Tipo de aislamiento'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)


class CleaningType(models.Model):
    """Model for 'Tipo de limpieza'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)
