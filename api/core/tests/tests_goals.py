
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from core.models import Goal
from core.serializers import GoalSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_goal(title: str, points: int):
        Goal.objects.create(title=title, points=points)

    def setUp(self):
        self.create_goal("abc", 1)
        self.create_goal("123", 2)
        self.create_goal("zyx", 3)
        self.create_goal("987", 9)
        self.create_goal("test", 8)

class GetAllGoalsTestCase(BaseViewTest):

    def test_get_all_goals(self):
        response = self.client.get(
            reverse("goals-all")
        )
        expected = Goal.objects.all()
        serialized = GoalSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
# Create your tests here.
