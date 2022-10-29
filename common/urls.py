from django.urls import path

from .views import LoginAPIVIew, RegisterAPIView

urlpatterns = [
  path('register', RegisterAPIView.as_view()),
  path('login', LoginAPIVIew.as_view())
]