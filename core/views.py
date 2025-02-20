from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from core.device_serializer import DeviceSerializer
from core.models import Device
from core.user_serializer import CustomTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    """class to obtain token by email"""

    serializer_class = CustomTokenObtainPairSerializer


class DeviceView(APIView):
    """
    View to list all devices
    """

    def get(self, request):
        if request.user.is_anonymous:
            return Response(
                {"message": "Hello, anonymous user!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        devices = Device.objects.filter(user=request.user)
        devices_serializer = DeviceSerializer(devices, many=True)
        return Response(devices_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.is_anonymous:
            return Response(
                {"message": "Hello, anonymous user!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        device_serializer = DeviceSerializer(data=request.data)
        if device_serializer.is_valid():
            device_serializer.save()
            return Response(device_serializer.data, status=status.HTTP_201_CREATED)
        return Response(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
