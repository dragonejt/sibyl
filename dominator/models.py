from django.db import models
from rest_framework.serializers import ModelSerializer
from community.models import Community

# Create your models here


class Actions(models.IntegerChoices):
    NOTIFY = 0
    REMOVE = 1
    MUTE = 2
    KICK = 3
    BAN = 4


class MessageDominator(models.Model):
    community = models.OneToOneField(Community, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Message Dominator"
        verbose_name_plural = "Message Dominators"

    def __str__(self) -> str:
        return f"{self.community.platform.username}/{self.community.community_id} ({self.id})"

    toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    toxicity_threshold = models.FloatField(default=0.5)

    severe_toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    severe_toxicity_threshold = models.FloatField(default=0.5)

    identity_attack_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    identity_attack_threshold = models.FloatField(default=0.5)

    insult_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    insult_threshold = models.FloatField(default=0.5)

    threat_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    threat_threshold = models.FloatField(default=0.5)

    profanity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    profanity_threshold = models.FloatField(default=0.5)

    sexually_explicit_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    sexually_explicit_threshold = models.FloatField(default=0.5)


class MemberDominator(models.Model):
    community = models.OneToOneField(Community, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Member Dominator"
        verbose_name_plural = "Member Dominators"

    def __str__(self) -> str:
        return f"{self.community.platform.username}/{self.community.community_id} ({self.id})"

    crime_coefficient_100_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    crime_coefficient_300_action = models.IntegerField(
        choices=Actions.choices, default=Actions.BAN)

    toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    toxicity_threshold = models.FloatField(default=0.5)

    severe_toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    severe_toxicity_threshold = models.FloatField(default=0.5)

    identity_attack_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    identity_attack_threshold = models.FloatField(default=0.5)

    insult_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    insult_threshold = models.FloatField(default=0.5)

    threat_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    threat_threshold = models.FloatField(default=0.5)

    profanity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    profanity_threshold = models.FloatField(default=0.5)

    sexually_explicit_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    sexually_explicit_threshold = models.FloatField(default=0.5)


class MemberDominatorSerializer(ModelSerializer):
    class Meta:
        model = MemberDominator
        fields = "__all__"


class MessageDominatorSerializer(ModelSerializer):
    class Meta:
        model = MessageDominator
        fields = "__all__"
