from rest_framework import serializers
from .models import User
#from django.contrib.auth import authenticate
#from django.contrib.auth.models import update_last_login


class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'last_login', 'last_request',)


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
