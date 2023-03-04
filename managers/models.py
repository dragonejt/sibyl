from django.db import models
from rest_framework.serializers import ModelSerializer
from profiles.models import CommunityProfile

# Create your models here.
DEFAULT_TRIGGER = {
    "action": "NOTIFY",
    "trigger": 0.5
}
DEFAULT_CC_TRIGGER = {
    "action": "NOTIFY",
    "trigger": 100
}


class MessageManager(models.Model):
    profile = models.OneToOneField(CommunityProfile, on_delete=models.CASCADE)

    # For Discord Servers Only
    discord_log_channel = models.CharField(max_length=20)
    discord_notify_role = models.CharField(max_length=20)

    crime_coefficient = models.JSONField(default=DEFAULT_CC_TRIGGER)
    toxicity = models.JSONField(default=DEFAULT_TRIGGER)
    severe_toxicity = models.JSONField(default=DEFAULT_TRIGGER)
    identity_attack = models.JSONField(default=DEFAULT_TRIGGER)
    insult = models.JSONField(default=DEFAULT_TRIGGER)
    threat = models.JSONField(default=DEFAULT_TRIGGER)
    profanity = models.JSONField(default=DEFAULT_TRIGGER)
    sexually_explicit = models.JSONField(default=DEFAULT_TRIGGER)


class MemberManager(models.Model):
    profile = models.OneToOneField(CommunityProfile, on_delete=models.CASCADE)

    # For Discord Servers Only
    discord_log_channel = models.CharField(max_length=20)
    discord_notify_role = models.CharField(max_length=20)

    crime_coefficient = models.JSONField(default=DEFAULT_CC_TRIGGER)
    toxicity = models.JSONField(default=DEFAULT_TRIGGER)
    severe_toxicity = models.JSONField(default=DEFAULT_TRIGGER)
    identity_attack = models.JSONField(default=DEFAULT_TRIGGER)
    insult = models.JSONField(default=DEFAULT_TRIGGER)
    threat = models.JSONField(default=DEFAULT_TRIGGER)
    profanity = models.JSONField(default=DEFAULT_TRIGGER)
    sexually_explicit = models.JSONField(default=DEFAULT_TRIGGER)


class MessageManagerSerializer(ModelSerializer):
    class Meta:
        model = MessageManager
        fields = "__all__"


class MemberManagerSerializer(ModelSerializer):
    class Meta:
        model = MemberManager
        fields = "__all__"
