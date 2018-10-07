
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rf_status
from rest_framework.permissions import AllowAny


class SendLoginEmailView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
       # make call to AWS SES
       pass
