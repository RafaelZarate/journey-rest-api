
from rest_framework import generics
from core.models import Task
from core.serializers import TaskSerializer

class ListTaskView(generics.ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
