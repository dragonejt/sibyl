from django.db import models
from rest_framework.serializers import ModelSerializer
from psychopass.models import CommunityPsychoPass

# Create your models here


class Actions(models.IntegerChoices):
    NOOP = 0
    NOTIFY = 1
    MUTE = 2
    KICK = 3
    BAN = 4


class MessageDominator(models.Model):
    profile = models.OneToOneField(
        CommunityPsychoPass, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Message Dominator"
        verbose_name_plural = "Message Dominators"

    def __str__(self) -> str:
        return f"{self.profile.platform}/{self.profile.platform_id}"

    # For Discord Servers Only
    discord_log_channel = models.CharField(
        max_length=20, blank=True, null=True)
    discord_notify_target = models.CharField(
        max_length=20, blank=True, null=True)

    toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    toxicity_trigger = models.FloatField(default=0.5)

    severe_toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    severe_toxicity_trigger = models.FloatField(default=0.5)

    identity_attack_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    identity_attack_trigger = models.FloatField(default=0.5)

    insult_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    insult_trigger = models.FloatField(default=0.5)

    threat_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    threat_trigger = models.FloatField(default=0.5)

    profanity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    profanity_trigger = models.FloatField(default=0.5)

    sexually_explicit_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    sexually_explicit_trigger = models.FloatField(default=0.5)


class MemberDominator(models.Model):
    profile = models.OneToOneField(
        CommunityPsychoPass, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Member Dominator"
        verbose_name_plural = "Member Dominators"

    def __str__(self) -> str:
        return f"{self.profile.platform}/{self.profile.platform_id}"

    # For Discord Servers Only
    discord_log_channel = models.CharField(
        max_length=20, blank=True, null=True)
    discord_notify_target = models.CharField(
        max_length=20, blank=True, null=True)

    crime_coefficient_100_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    crime_coefficient_300_action = models.IntegerField(
        choices=Actions.choices, default=Actions.BAN)

    toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    toxicity_trigger = models.FloatField(default=0.5)

    severe_toxicity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    severe_toxicity_trigger = models.FloatField(default=0.5)

    identity_attack_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    identity_attack_trigger = models.FloatField(default=0.5)

    insult_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    insult_trigger = models.FloatField(default=0.5)

    threat_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    threat_trigger = models.FloatField(default=0.5)

    profanity_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    profanity_trigger = models.FloatField(default=0.5)

    sexually_explicit_action = models.IntegerField(
        choices=Actions.choices, default=Actions.NOTIFY)
    sexually_explicit_trigger = models.FloatField(default=0.5)


class MemberDominatorSerializer(ModelSerializer):
    class Meta:
        model = MemberDominator
        fields = "__all__"

class MessageDominatorSerializer(ModelSerializer):
    class Meta:
        model = MessageDominator
        fields = "__all__"
