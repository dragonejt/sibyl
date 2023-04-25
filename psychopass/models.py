from django.db import models
from django.contrib.auth import get_user_model
from community.models import Community
from rest_framework.serializers import ModelSerializer

# Create your models here


class UserPsychoPass(models.Model):
    platform = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20, unique=True)

    messages = models.PositiveBigIntegerField(default=0)
    psycho_hazard = models.BooleanField(default=False)

    toxicity = models.FloatField(default=0.5)
    severe_toxicity = models.FloatField(default=0.5)
    identity_attack = models.FloatField(default=0.5)
    insult = models.FloatField(default=0.5)
    threat = models.FloatField(default=0.5)
    profanity = models.FloatField(default=0.5)
    sexually_explicit = models.FloatField(default=0.5)

    class Meta:
        verbose_name = "Psycho-Pass"
        verbose_name_plural = "Psycho-Passes"

    def __str__(self) -> str:
        return f"{self.platform.username}/{self.user_id} ({self.id})"

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
        self.messages = max(0, min(500, self.messages+1))

    def crime_coefficient(self) -> int:
        base = 100
        base += (self.toxicity - 0.5) * 500
        base += max(0, (self.severe_toxicity - 0.5)) * 50
        base += max(0, (self.identity_attack - 0.5)) * 50
        base += max(0, (self.insult - 0.5)) * 50
        base += max(0, (self.threat - 0.5)) * 50
        base += max(0, (self.profanity - 0.5)) * 50
        base += max(0, (self.sexually_explicit - 0.5)) * 50
        return int(max(0, min(500, base)))

    def hue(self) -> str:
        return "{}{}{}{}{}{}".format(
            self.get_hex(self.threat),
            self.get_hex(self.sexually_explicit),
            self.get_hex(self.insult),
            self.get_hex(self.identity_attack),
            self.get_hex(self.toxicity),
            self.get_hex(self.severe_toxicity)
        )

    def update_score(self, attr: dict, field: float, denom: int) -> float:
        attribute_score = attr.get("summaryScore").get("value")
        score = (attribute_score + field * denom)/(denom + 1)
        return max(0, min(1, score))

    def get_hex(self, score: float) -> str:
        div = 1.0 / 16
        i = max(0, min(15, 15 - int(score / div)))
        return f"{i:x}".capitalize()


class CommunityPsychoPass(models.Model):
    community = models.OneToOneField(Community, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserPsychoPass, blank=True)

    class Meta:
        verbose_name = "Community Psycho-Pass"
        verbose_name_plural = "Community Psycho-Passes"

    def __str__(self) -> str:
        return f"{self.platform.username}/{self.community_id} ({self.id})"

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


class UserPsychoPassSerializer(ModelSerializer):
    class Meta:
        model = UserPsychoPass
        fields = "__all__"


class CommunityPsychoPassSerializer(ModelSerializer):
    class Meta:
        model = CommunityPsychoPass
        fields = "__all__"
