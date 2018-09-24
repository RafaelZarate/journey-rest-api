
from rest_framework import generics
from core.models import Journey
from core.serializers import JourneySerializer

class ListJourneyView(generics.ListAPIView):

    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
