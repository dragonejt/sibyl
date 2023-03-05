from django.urls import path
from profiles import views

urlpatterns = [
    path("user", views.UserProfileView.as_view()),
    path("community", views.CommunityProfileView.as_view()),
    path("message", views.ingest_message)
]
