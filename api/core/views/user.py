
from rest_framework import generics
from .models import Goal
from .serializers import GoalSerializer

class ListGoalsView(generics.ListAPIView):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

