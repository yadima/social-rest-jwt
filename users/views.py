#from django.shortcuts import render
#from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserActivitySerializer
from .models import User
#from rest_framework import generics, viewsets

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        if user.is_authenticated:
            User.objects.filter(id=user.id).update(last_login=timezone.now())

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)


class UsersActivityView(APIView):

    @staticmethod
    def get(request):
        """
        List posts
        """

        users = User.objects.all()
        return Response(UserActivitySerializer(users, many=True).data)
