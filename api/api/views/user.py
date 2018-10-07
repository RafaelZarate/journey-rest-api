
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rf_status
from rest_framework.permissions import AllowAny

from core.models import User
from core.serializers import UserSerializer

class ListUserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDataView(APIView):

    permission_classes = (AllowAny, )
    def get(self, request):
        return Response(
            dict(
                id=1,
                first_name='Rafael'
            ),
            status=rf_status.HTTP_200_OK
        )
