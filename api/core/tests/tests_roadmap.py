
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from database.generators.roadmap import create_roadmap
from core.models import RoadMap
from core.serializers import RoadMapSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        create_roadmap()
        create_roadmap()
        create_roadmap()
        create_roadmap()

class GetAllGoalsTestCase(BaseViewTest):

    def test_get_all_goals(self):
        response = self.client.get(
            reverse("roadmap-all")
        )
        expected = RoadMap.objects.all()
        serialized = RoadMapSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
# Create your tests here.
