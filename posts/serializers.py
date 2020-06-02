from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title','body')


class PostSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('user','title','body')
