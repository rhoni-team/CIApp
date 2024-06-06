"""module with serializers for disease model"""
from rest_framework import serializers
from backend.models import Disease


class DiseasesNamesSerializer(serializers.ModelSerializer):
    """diseases names and labels model serializer"""
    
    class Meta:
        model = Disease
        fields = ['id', 'name', 'label']


class CompleteDataDiseaseSerializer(serializers.ModelSerializer):
    """diseases serializer with all their data"""

    class Meta:
        model = Disease
        fields = "__all__"
        depth = 1