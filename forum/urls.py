from django.urls import path
from forum.views.user_views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"), 
]