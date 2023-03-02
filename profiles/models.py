import sys
from django.db import models
from datetime import datetime
from rest_framework.serializers import ModelSerializer
from clients.discord import get_server_info

# Create your models here.


def update_score(attr: dict, field: float, denom: int) -> float:
    score = attr.get("summaryScore").get("value")
    return (score + field * denom)/(denom + 1)


class ToxicityProfile(models.Model):
    platform = models.CharField(max_length=20)
    platform_id = models.CharField(max_length=20)
    last_flag = models.DateTimeField(auto_now_add=True, blank=True)

    toxicity = models.FloatField(default=0.5)
    severe_toxicity = models.FloatField(default=0.5)
    identity_attack = models.FloatField(default=0.5)
    insult = models.FloatField(default=0.5)
    threat = models.FloatField(default=0.5)
    profanity = models.FloatField(default=0.5)
    sexually_explicit = models.FloatField(default=0.5)

    class Meta:
        abstract = True


class UserProfile(ToxicityProfile):
    messages = models.PositiveBigIntegerField(default=0)
    psycho_hazard = models.BooleanField(default=False)

    def ingest_message(self, scores: dict) -> None:
        self.toxicity = update_score(
            scores.get("TOXICITY"), self.toxicity, self.messages)
        self.severe_toxicity = update_score(
            scores.get("SEVERE_TOXICITY"), self.severe_toxicity, self.messages)
        self.identity_attack = update_score(
            scores.get("IDENTITY_ATTACK"), self.identity_attack, self.messages)
        self.insult = update_score(
            scores.get("INSULT"), self.insult, self.messages)
        self.threat = update_score(
            scores.get("THREAT"), self.threat, self.messages)
        self.profanity = update_score(
            scores.get("PROFANITY"), self.profanity, self.messages)
        self.sexually_explicit = update_score(
            scores.get("SEXUALLY_EXPLICIT"), self.sexually_explicit, self.messages)
        for attr, score in scores.items():
            if score > 0.5:
                self.last_flag = datetime.utcnow()
                break
        self.messages += 1

    def crime_coefficient(self) -> float:
        return self.toxicity

    def hue(self) -> str:
        return "#FFFFFF"


class CommunityProfile(ToxicityProfile):
    users = models.PositiveIntegerField(default=0)

    def ingest_message(self, scores: dict) -> None:
        if self.platform == "discord":
            self.users = get_server_info(
                request.data.get("communityID")).get("approximate_member_count")
        self.toxicity = update_score(
            scores.get("TOXICITY"), self.toxicity, self.users)
        self.severe_toxicity = update_score(
            scores.get("SEVERE_TOXICITY"), self.severe_toxicity, self.users)
        self.identity_attack = update_score(
            scores.get("IDENTITY_ATTACK"), self.identity_attack, self.users)
        self.insult = update_score(
            scores.get("INSULT"), self.insult, self.users)
        self.threat = update_score(
            scores.get("THREAT"), self.threat, self.users)
        self.profanity = update_score(
            scores.get("PROFANITY"), self.profanity, self.users)
        self.sexually_explicit = update_score(
            scores.get("SEXUALLY_EXPLICIT"), self.sexually_explicit, self.users)
        for attr, score in scores.items():
            if score > 0.5:
                self.last_flag = datetime.utcnow()
                break

    def area_stress_level(self) -> int:
        return 0


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CommunityProfileSerializer(ModelSerializer):
    class Meta:
        model = CommunityProfile
        fields = "__all__"
