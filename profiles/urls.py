from django.urls import path
from profiles import views

urlpatterns = [
    path("user/", views.UserProfiles.as_view()),
    path("", views.ingest_message)
]