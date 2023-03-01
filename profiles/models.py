import sys
from django.db import models
from datetime import datetime
from rest_framework.serializers import ModelSerializer

# Create your models here.


def avg(new: float, score: float, denominator: int) -> float:
    return (new + score * denominator)/(denominator + 1)


class ToxicityProfile(models.Model):
    platform = models.CharField(max_length=20)
    platform_id = models.CharField(max_length=20)
    last_flag = models.DateTimeField()

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
    messages = models.PositiveBigIntegerField()
    psycho_hazard = models.BooleanField(default=False)

    def ingest_message(self, scores: dict) -> None:
        self.toxicity = avg(scores.get("toxicity"),
                            self.toxicity, self.messages)
        self.identity_attack = avg(scores.get("identity_attack"),
                                   self.identity_attack, self.messages)
        self.insult = avg(scores.get("insult"),
                          self.insult, self.messages)
        self.threat = avg(scores.get("threat"),
                          self.threat, self.messages)
        self.profanity = avg(scores.get("profanity"),
                             self.profanity, self.messages)
        self.sexually_explicit = avg(scores.get("sexually_explicit"),
                                     self.sexually_explicit, self.messages)
        for attr, score in scores.items():
            if score > 0.5:
                self.last_flag = datetime.utcnow()
        self.messages += 1

    def crime_coefficient(self) -> float:
        return self.toxicity

    def hue(self) -> str:
        return "#FFFFFF"


class ServerProfile(ToxicityProfile):
    users = models.PositiveIntegerField()

    def ingest_message(self, scores: dict) -> None:
        self.toxicity = avg(scores.get("toxicity"),
                            self.toxicity, self.users)
        self.identity_attack = avg(scores.get("identity_attack"),
                                   self.identity_attack, self.users)
        self.insult = avg(scores.get("insult"),
                          self.insult, self.users)
        self.threat = avg(scores.get("threat"),
                          self.threat, self.users)
        self.profanity = avg(scores.get("profanity"),
                             self.profanity, self.users)
        self.sexually_explicit = avg(scores.get("sexually_explicit"),
                                     self.sexually_explicit, self.users)
        for attr, score in scores.items():
            if score > 0.5:
                self.last_flag = datetime.utcnow()

    def area_stress_level(self) -> int:
        return 0


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class ServerProfileSerializer(ModelSerializer):
    class Meta:
        model = ServerProfile
        fields = "__all__"
