from django.conf.urls import url
from .views import PostView


urlpatterns = [

    # Posts
    url(r'^posts/', PostView.as_view()),

]