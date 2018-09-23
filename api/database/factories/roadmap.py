
from factory import SubFactory
from factory.django import DjangoModelFactory

from database.factories.user import UserFactory

class RoadMapFactory(DjangoModelFactory):
    class Meta:
        model = 'core.RoadMap'

    user = SubFactory(UserFactory)
    due_date = '2019-01-01'
