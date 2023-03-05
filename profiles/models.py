from django.db import models
from django.utils.timezone import now
from rest_framework.serializers import ModelSerializer

# Create your models here


class UserProfile(models.Model):
    platform = models.CharField(max_length=20)
    platform_id = models.CharField(max_length=20, unique=True)
    last_flag = models.DateTimeField(default=now, blank=True)
    messages = models.PositiveBigIntegerField(default=0)
    psycho_hazard = models.BooleanField(default=False)

    toxicity = models.FloatField(default=0.5)
    severe_toxicity = models.FloatField(default=0.5)
    identity_attack = models.FloatField(default=0.5)
    insult = models.FloatField(default=0.5)
    threat = models.FloatField(default=0.5)
    profanity = models.FloatField(default=0.5)
    sexually_explicit = models.FloatField(default=0.5)

    def __str__(self) -> str:
        return f"{self.platform}/{self.platform_id}"

    def ingest_message(self, scores: dict) -> None:
        self.toxicity = self.update_score(
            scores.get("TOXICITY"), self.toxicity, self.messages)
        self.severe_toxicity = self.update_score(
            scores.get("SEVERE_TOXICITY"), self.severe_toxicity, self.messages)
        self.identity_attack = self.update_score(
            scores.get("IDENTITY_ATTACK"), self.identity_attack, self.messages)
        self.insult = self.update_score(
            scores.get("INSULT"), self.insult, self.messages)
        self.threat = self.update_score(
            scores.get("THREAT"), self.threat, self.messages)
        self.profanity = self.update_score(
            scores.get("PROFANITY"), self.profanity, self.messages)
        self.sexually_explicit = self.update_score(
            scores.get("SEXUALLY_EXPLICIT"), self.sexually_explicit, self.messages)
        for attr, score in scores.items():
            if score.get("summaryScore").get("value") > 0.5:
                self.last_flag = now()
                break
        self.messages = max(0, min(500, self.messages+1))

    def crime_coefficient(self) -> int:
        base = 100
        base += (self.toxicity - 0.5) * 500
        base += (self.severe_toxicity - 0.5) * 50
        base += (self.identity_attack - 0.5) * 50
        base += (self.insult - 0.5) * 50
        base += (self.threat - 0.5) * 50
        base += (self.profanity - 0.5) * 50
        base += (self.sexually_explicit - 0.5) * 50
        return int(max(0, min(500, base)))

    def hue(self) -> str:
        return "#{}{}{}{}{}{}".format(
            self.get_hex(self.threat),
            self.get_hex(self.sexually_explicit),
            self.get_hex(self.identity_attack),
            self.get_hex(self.insult),
            self.get_hex(self.severe_toxicity),
            self.get_hex(self.toxicity)
        )

    def update_score(self, attr: dict, field: float, denom: int) -> float:
        attribute_score = attr.get("summaryScore").get("value")
        score = (attribute_score + field * denom)/(denom + 1)
        return max(0, min(1, score))

    def get_hex(self, score: float) -> str:
        div = 1.0 / 16
        i = max(0, min(15, 15 - int(score / div)))
        return f"{i:x}".capitalize()


class CommunityProfile(models.Model):
    platform = models.CharField(max_length=20)
    platform_id = models.CharField(max_length=20, unique=True)
    users = models.ManyToManyField(UserProfile, blank=True)

    def __str__(self) -> str:
        return f"{self.platform}/{self.platform_id}"

    def area_stress_level(self) -> dict:
        return {
            "toxicity": self.toxicity(),
            "severe_toxicity": self.severe_toxicity(),
            "identity_attack": self.identity_attack(),
            "insult": self.insult(),
            "threat": self.threat(),
            "profanity": self.profanity(),
            "sexually_explicit": self.sexually_explicit()
        }

    def toxicity(self) -> float:
        return self.users.aggregate(models.Avg("toxicity")).get("toxicity__avg")

    def severe_toxicity(self) -> float:
        return self.users.aggregate(models.Avg("severe_toxicity")).get("severe_toxicity__avg")

    def identity_attack(self) -> float:
        return self.users.aggregate(models.Avg("identity_attack")).get("identity_attack__avg")

    def insult(self) -> float:
        return self.users.aggregate(models.Avg("insult")).get("insult__avg")

    def threat(self) -> float:
        return self.users.aggregate(models.Avg("threat")).get("threat__avg")

    def profanity(self) -> float:
        return self.users.aggregate(models.Avg("profanity")).get("profanity__avg")

    def sexually_explicit(self) -> float:
        return self.users.aggregate(models.Avg("sexually_explicit")).get("sexually_explicit__avg")


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CommunityProfileSerializer(ModelSerializer):
    class Meta:
        model = CommunityProfile
        fields = "__all__"
