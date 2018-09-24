
from factory import SubFactory
from factory.django import DjangoModelFactory

from database.factories.roadmap import RoadMapFactory

class JourneyFactory(DjangoModelFactory):
    class Meta:
        model = 'core.Journey'

    type = 1
    status = 1
    roadmap = SubFactory(RoadMapFactory)
