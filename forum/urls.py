from django.urls import path
from forum.views.user_views import UserRegisterView, UserLoginView
from forum.views.topic_views import TopicListView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"), 
    path("login/", UserLoginView.as_view(), name="login"),
    path("index/", TopicListView.as_view(), name="index"),
]