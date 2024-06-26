# Generated by Django 4.1.7 on 2023-04-11 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPsychoPass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=20, unique=True)),
                (
                    "last_flag",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                ("messages", models.PositiveBigIntegerField(default=0)),
                ("psycho_hazard", models.BooleanField(default=False)),
                ("toxicity", models.FloatField(default=0.5)),
                ("severe_toxicity", models.FloatField(default=0.5)),
                ("identity_attack", models.FloatField(default=0.5)),
                ("insult", models.FloatField(default=0.5)),
                ("threat", models.FloatField(default=0.5)),
                ("profanity", models.FloatField(default=0.5)),
                ("sexually_explicit", models.FloatField(default=0.5)),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Psycho-Pass",
                "verbose_name_plural": "Psycho-Passes",
            },
        ),
        migrations.CreateModel(
            name="CommunityPsychoPass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("community_id", models.CharField(max_length=20, unique=True)),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(blank=True, to="psychopass.userpsychopass"),
                ),
            ],
            options={
                "verbose_name": "Community Psycho-Pass",
                "verbose_name_plural": "Community Psycho-Passes",
            },
        ),
    ]
