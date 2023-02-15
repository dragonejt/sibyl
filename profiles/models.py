from django.db import models

# Create your models here.


class ToxicityProfile(models.Model):

    toxicity = models.FloatField(default=0.5)
    last_toxic_message = models.DateTimeField()

    severe_toxicity = models.FloatField(default=0.5)
    identity_attack = models.FloatField(default=0.5)
    insult = models.FloatField(default=0.5)
    threat = models.FloatField(default=0.5)
    profanity = models.FloatField(default=0.5)
    sexually_explicit = models.FloatField(default=0.5)

    def ingest_message(self, message: str, scores: dict) -> None:
        self.toxicity = scores.get("toxicity")
        self.identity_attack = scores.get("identity_attack")
        self.insult = scores.get("insult")
        self.threat = scores.get("threat")
        self.profanity = scores.get("profanity")
        self.sexually_explicit = scores.get("sexually_explicit")


class UserProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()
    messages = models.PositiveBigIntegerField()
    psycho_hazard = models.BooleanField(default=False)

    def ingest_message(self, message: str, scores: dict) -> None:
        super().ingest_message(message, scores)
        
        self.messages += 1

    def crime_coefficient(self) -> float:
        return self.toxicity

    def hue(self) -> str:
        return "#FFFFFF"


class ServerProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()

    def area_stress_level(self) -> int:
        return 0
