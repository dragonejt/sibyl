from django.urls import path
from managers import views

urlpatterns = [
    path("message", views.MessageManagerView.as_view()),
    path("member", views.MemberManagerView.as_view())
]
