"""sibyl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny
from community.views import CommunityView
from psychopass.views import UserPsychoPassView, CommunityPsychoPassView, ingest_message
from dominator.views import MessageDominatorView, MemberDominatorView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("community", CommunityView.as_view()),
    path("psychopass/user", UserPsychoPassView.as_view()),
    path("psychopass/community", CommunityPsychoPassView.as_view()),
    path("psychopass/message", ingest_message),
    path("dominator/message", MessageDominatorView.as_view()),
    path("dominator/member", MemberDominatorView.as_view()),
    path(
        "sibyl-schema.yml",
        get_schema_view(
            title="Sibyl System API",
            description="AutoMod and Toxicity Profiles using ML",
            permission_classes=[AllowAny],
        ),
        name="sibyl-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "sibyl-schema"},
        ),
        name="swagger-ui",
    ),
]
