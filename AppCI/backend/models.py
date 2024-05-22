"""Models for backend app"""
from django.db import models


class IsolationType(models.Model):
    """Model for 'Tipo de aislamiento'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=True, blank=True)

