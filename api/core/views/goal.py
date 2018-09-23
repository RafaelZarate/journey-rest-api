
from rest_framework import generics
from core.models import Goal
from core.serializers import GoalSerializer

class ListGoalsView(generics.ListAPIView):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

