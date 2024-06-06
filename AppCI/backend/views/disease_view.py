from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Disease
from backend.serializers.disease_serializer import ListDiseasesSerializer


class DiseasesListView(APIView):
    """View for diseases"""

    def get(self, request):
        """retrieve all the diseases objects"""
        instance = Disease.objects.all()
        serializer = ListDiseasesSerializer(instance, many=True)
        return Response(serializer.data)
