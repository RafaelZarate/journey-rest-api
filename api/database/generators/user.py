
from database.factories.user import UserFactory

def create_user(**kwargs):
    UserFactory.create(**kwargs)
