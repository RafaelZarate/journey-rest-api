
from database.factories.journey import JourneyFactory

def create_journey(**kwargs):
    JourneyFactory.create(**kwargs)