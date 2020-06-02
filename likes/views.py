from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Like
from .serializers import PostLikeSerializer, PostLikeSerializerCreate, PostLikeSerializerAnalyticsByDay
from django.db.models import Count

# Like
class PostLikeView(APIView):

    @staticmethod
    def post(request):
        """
        Create like
        """

        serializer = PostLikeSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostLikeSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Unlike: delete post_unlike/{post_id}
class PostDislike(APIView):

    @staticmethod
    def delete(request, post_id):
        """
        Unlike/Delete a like
        """

        post_like = get_object_or_404(Like, post=post_id, user=request.user)
        if post_like.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post_like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Analytics by day
class PostLikeAnalyticsByDayView(APIView):
    
    @staticmethod
    def get(request):
        """
        Count likes by day
        """
        
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        likes = Like.objects.filter(date__range=[date_from, date_to]).values('date').annotate(likes_per_day=Count('date'))
        return Response(PostLikeSerializerAnalyticsByDay(likes, many=True).data)
