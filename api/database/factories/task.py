
from factory import SubFactory
from factory.django import DjangoModelFactory

from database.factories.journey import JourneyFactory

class TaskFactory(DjangoModelFactory):
    class Meta:
        model = 'core.Task'

    journey = SubFactory(JourneyFactory)
    status = 1
