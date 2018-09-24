
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from database.generators.user import create_user
from core.models import User
from core.serializers import UserSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        create_user()
        create_user()
        create_user()
        create_user()
        create_user()

class GetAllGoalsTestCase(BaseViewTest):

    def test_get_all_goals(self):
        response = self.client.get(
            reverse("user-all")
        )
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
# Create your tests here.
