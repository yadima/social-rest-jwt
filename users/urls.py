from django.conf.urls import url
from users.views import UserRegistrationView, UsersActivityView


urlpatterns = [
    #url(r'^token/', CustomTokenObtainPairView.as_view()),
    url(r'^signup/', UserRegistrationView.as_view()),
    url(r'^users_activity/', UsersActivityView.as_view()),
    ]