from django.db import models

# Create your models here.


class ToxicityProfile(models.Model):

    toxicity = models.FloatField()

    severe_toxicity = models.FloatField()
    identity_attack = models.FloatField()
    insult = models.FloatField()
    threat = models.FloatField()
    profanity = models.FloatField()
    sexually_explicit = models.FloatField()

    def ingest_message(self, message: dict) -> None:
        pass


class UserProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()
    psycho_hazard = models.BooleanField(default=False)

    def crime_coefficient(self) -> float:
        return self.toxicity

    def hue(self) -> str:
        return "#FFFFFF"


class ServerProfile(ToxicityProfile):

    discordID = models.PositiveBigIntegerField()

    def area_stress_level(self) -> int:
        return 0
