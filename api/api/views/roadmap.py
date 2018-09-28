
from rest_framework import generics
from core.models import RoadMap
from core.serializers import RoadMapSerializer

class ListRoadMapView(generics.ListAPIView):

    queryset = RoadMap.objects.all()
    serializer_class = RoadMapSerializer
