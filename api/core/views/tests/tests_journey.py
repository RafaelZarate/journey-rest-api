
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from database.generators.journey import create_journey
from core.models import Journey
from core.serializers import JourneySerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        create_journey()
        create_journey()
        create_journey()
        create_journey()
        create_journey()

class GetAllJourneysTestCase(BaseViewTest):

    def test_get_all_goals(self):
        response = self.client.get(
            reverse("journey-all")
        )
        expected = Journey.objects.all()
        serialized = JourneySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
