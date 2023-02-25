from django.db import models
from datetime import datetime

# Create your models here.

class ToxicityProfile(models.Model):

    toxicity = models.FloatField(default=0.5)
    last_message = models.DateTimeField()
    denominator = float("inf")

    severe_toxicity = models.FloatField(default=0.5)
    identity_attack = models.FloatField(default=0.5)
    insult = models.FloatField(default=0.5)
    threat = models.FloatField(default=0.5)
    profanity = models.FloatField(default=0.5)
    sexually_explicit = models.FloatField(default=0.5)

    def ingest_message(self, scores: dict) -> None:
        self.toxicity = (scores.get("toxicity") + self.toxicity * self.denominator)/(self.denominator + 1)
        self.identity_attack = (scores.get("identity_attack") + self.identity_attack * self.denominator)/(self.denominator + 1)
        self.insult = (scores.get("insult") + self.insult * self.denominator)/(self.denominator + 1)
        self.threat = (scores.get("threat") + self.toxicity * self.denominator)/(self.denominator + 1)
        self.profanity = (scores.get("profanity") + self.profanity * self.denominator)/(self.denominator + 1)
        self.sexually_explicit = (scores.get("sexually_explicit") + self.sexually_explicit * self.denominator)/(self.denominator + 1)
        self.last_message = datetime.utcnow()

class UserProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()
    messages = models.PositiveBigIntegerField()
    psycho_hazard = models.BooleanField(default=False)
    denominator = messages

    def ingest_message(self, scores: dict) -> None:
        super().ingest_message(scores)
        self.messages += 1

    def crime_coefficient(self) -> float:
        return self.toxicity

    def hue(self) -> str:
        return "#FFFFFF"


class ServerProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()
    users = models.PositiveIntegerField()
    denominator = users

    def area_stress_level(self) -> int:
        return 0
