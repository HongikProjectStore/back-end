from django.urls import path
from .views import SignUpView, SignInView, ProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/', SignInView.as_view()),
    path('profile/<int:pk>/',ProfileView.as_view()),
]