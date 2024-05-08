from django.urls import path
from psychopass import views

urlpatterns = [
    path("user", views.UserPsychoPassView.as_view()),
    path("community", views.CommunityPsychoPassView.as_view()),
    path("message", views.ingest_message),
]
