from django.urls import path
from community.views import CommunityView

urlpatterns = [
    path("", CommunityView.as_view())
]
