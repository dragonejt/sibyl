from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

# Create your models here.


class Community(models.Model):
    platform = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    community_id = models.CharField(max_length=20, unique=True)

    # For Discord Servers Only
    discord_log_channel = models.CharField(
        max_length=20, blank=True, null=True)
    discord_notify_target = models.CharField(
        max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.platform.username}/{self.community_id}"


class CommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"
