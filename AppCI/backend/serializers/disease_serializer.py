"""module with serializers for disease model"""
from rest_framework import serializers
from backend.models import Disease


class ListDiseasesSerializer(serializers.ModelSerializer):
    """list of diseases model serializer"""
    
    class Meta:
        model = Disease
        fields = ['id', 'name', 'label']
        depth = 1
