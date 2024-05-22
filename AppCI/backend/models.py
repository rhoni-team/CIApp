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


class UnitsOfTime(models.Model):
    """Model with units of time"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)


class IsolationTime(models.Model):
    """Model for 'Tiempo de Aislamiento'"""
    name = models.CharField(max_length=300, blank=True, null=True)
    label = models.CharField(max_length=300, null=True, blank=True)
    isolation_time = models.IntegerField(blank=True, null=True)
    isolation_unit = models.ForeignKey('UnitsOfTime', models.SET_NULL, blank=True, null=True)
    with_atb = models.BooleanField(blank=True, null=True)
    other_isolation = models.CharField(max_length=500, null=True, blank=True)


class IsolationWarnings(models.Model):
    """Model for 'Advertencias'"""
    name = models.CharField(max_length=300, null=False, blank=False)
    label = models.CharField(max_length=300, null=True, blank=True)


class DiseaseType(models.Model):
    """Model for 'Tipo de enfermedad'"""
    name = models.CharField(max_length=300, null=False, blank=False)
    label = models.CharField(max_length=300, null=True, blank=True)
