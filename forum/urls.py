from django.urls import path
from forum.views.user_views import UserRegisterView, UserLoginView
from forum.views.topic_views import TopicListView, TopicRegistrationView, TopicVisualizationView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"), 
    path("login/", UserLoginView.as_view(), name="login"),
    path("index/", TopicListView.as_view(), name="index"),
    path("topic/", TopicRegistrationView.as_view(), name="topic"),
    path("topic/<int:topic_id>/", TopicVisualizationView.as_view(), name="topic-visualization"),
]