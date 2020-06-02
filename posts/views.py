from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from posts.serializers import PostSerializer, PostSerializerCreate


# Posts
class PostView(APIView):

    @staticmethod
    def get(request):
        """
        List posts
        """

        posts = Post.objects.all()
        #serializer_class = PostSerializer
        return Response(PostSerializer(posts, many=True).data)
        
    @staticmethod
    def post(request):
        """
        Create post
        """

        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
