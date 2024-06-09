from django.urls import path
from .views import UserView, ActivateUserView


urlpatterns = [
    path("register", UserView.as_view()),
    path("activate", ActivateUserView.as_view()),
]
