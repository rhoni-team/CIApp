"""Models for backend app"""
from django.db import models


class PrecautionType(models.Model):
    """Model for 'Tipo de precaución'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)


class CleaningType(models.Model):
    """Model for 'Tipo de limpieza'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.label


class UnitsOfTime(models.Model):
    """Model with units of time"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)


class SpecialCasesIsolationTime(models.Model):
    """Special cases of isolation time for some diseases"""
    disease_name = models.CharField(max_length=100, null=False, blank=False)
    isolation_time = models.CharField(max_length=300, null=True, blank=True)


class IsolationWarnings(models.Model):
    """Model for 'Advertencias'"""
    name = models.CharField(max_length=300, null=False, blank=False)
    label = models.CharField(max_length=300, null=True, blank=True)


class DiseaseType(models.Model):
    """Model for 'Tipo de enfermedad'"""
    name = models.CharField(max_length=300, null=False, blank=False)
    label = models.CharField(max_length=300, null=True, blank=True)


class Disease(models.Model):
    """Model for 'enfermedad'"""
    name = models.CharField(max_length=100, null=False, blank=False)
    label = models.CharField(max_length=100, null=True, blank=True)
    disease_type = models.ForeignKey(DiseaseType, models.SET_NULL, blank=True, null=True)
    precaution_type = models.ForeignKey(PrecautionType, models.SET_NULL, blank=True, null=True)
    cleaning_type = models.ManyToManyField(CleaningType, blank=True, null=True, related_name='diseases')
    isolation_time = models.IntegerField(blank=True, null=True)
    isolation_unit = models.ForeignKey("UnitsOfTime", models.SET_NULL, blank=True, null=True)
    with_atb = models.BooleanField(blank=True, null=True)
    other_isolation = models.ForeignKey(SpecialCasesIsolationTime, models.SET_NULL, blank=True, null=True)
    mandatory_declaration = models.BooleanField(null=True, blank=True)
    room_sharing = models.BooleanField(null=True, blank=True)
    isolation_warnings = models.ForeignKey(IsolationWarnings, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.label
