from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from backend.models import Disease
from backend.serializers.disease_serializer import DiseasesNamesSerializer, CompleteDataDiseaseSerializer
from backend.views.utils.reorder_api_data import ReorderAPIData


class DiseasesListView(APIView):
    """View for diseases"""

    def get(self, request):
        """retrieve all the diseases objects"""
        instance = Disease.objects.all()
        serializer = DiseasesNamesSerializer(instance, many=True)
        return Response(serializer.data)
    

class DetailedDisease(APIView):
    """retrieve the detail for only one disease"""

    def get(self, request, disease_id):
        """get one disease object from its id"""
        disease_instance = get_object_or_404(Disease, pk=disease_id)
        serializer = CompleteDataDiseaseSerializer(disease_instance)
        detailed_data = serializer.data
        utils_order_data = ReorderAPIData(disease_data=detailed_data)
        ordered_detailed_data = utils_order_data.reorder_data()
        return Response(data=ordered_detailed_data)
