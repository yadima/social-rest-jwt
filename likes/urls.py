from django.conf.urls import url
from .views import PostLikeView, PostDislike, PostLikeAnalyticsByDayView


urlpatterns = [

    # Post likes/unlikes
    url(r'^post_like/', PostLikeView.as_view()),
    url(r'^post_unlike/(?P<post_id>[\d]+)$', PostDislike.as_view()),
    url(r'^analytics/', PostLikeAnalyticsByDayView.as_view()),

]