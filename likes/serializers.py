from rest_framework import serializers
from .models import Like
#from django.db.models import Count


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('post', 'date',)


class PostLikeSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = '__all__'


class PostLikeSerializerAnalyticsByDay(serializers.ModelSerializer):
    likes_per_day = serializers.IntegerField(read_only=True)
    class Meta:
        model = Like
        fields = ('date', 'likes_per_day',)
