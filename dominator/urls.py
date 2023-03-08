from django.urls import path
from dominator import views

urlpatterns =[
    path("message", views.MessageDominatorView.as_view()),
    path("member", views.MemberDominatorView.as_view())
]