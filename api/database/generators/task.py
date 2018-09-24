
from database.factories.task import TaskFactory

def create_task(**kwargs):
    TaskFactory.create(**kwargs)