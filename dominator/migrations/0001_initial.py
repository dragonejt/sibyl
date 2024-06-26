# Generated by Django 4.1.7 on 2023-04-11 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("psychopass", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageDominator",
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
                (
                    "discord_log_channel",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "discord_notify_target",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "toxicity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("toxicity_threshold", models.FloatField(default=0.5)),
                (
                    "severe_toxicity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("severe_toxicity_threshold", models.FloatField(default=0.5)),
                (
                    "identity_attack_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("identity_attack_threshold", models.FloatField(default=0.5)),
                (
                    "insult_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("insult_threshold", models.FloatField(default=0.5)),
                (
                    "threat_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("threat_threshold", models.FloatField(default=0.5)),
                (
                    "profanity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("profanity_threshold", models.FloatField(default=0.5)),
                (
                    "sexually_explicit_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("sexually_explicit_threshold", models.FloatField(default=0.5)),
                (
                    "psycho_pass",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychopass.communitypsychopass",
                    ),
                ),
            ],
            options={
                "verbose_name": "Message Dominator",
                "verbose_name_plural": "Message Dominators",
            },
        ),
        migrations.CreateModel(
            name="MemberDominator",
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
                (
                    "discord_log_channel",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "discord_notify_target",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "crime_coefficient_100_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "crime_coefficient_300_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=4,
                    ),
                ),
                (
                    "toxicity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("toxicity_threshold", models.FloatField(default=0.5)),
                (
                    "severe_toxicity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("severe_toxicity_threshold", models.FloatField(default=0.5)),
                (
                    "identity_attack_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("identity_attack_threshold", models.FloatField(default=0.5)),
                (
                    "insult_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("insult_threshold", models.FloatField(default=0.5)),
                (
                    "threat_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("threat_threshold", models.FloatField(default=0.5)),
                (
                    "profanity_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("profanity_threshold", models.FloatField(default=0.5)),
                (
                    "sexually_explicit_action",
                    models.IntegerField(
                        choices=[
                            (0, "Noop"),
                            (1, "Notify"),
                            (2, "Mute"),
                            (3, "Kick"),
                            (4, "Ban"),
                        ],
                        default=1,
                    ),
                ),
                ("sexually_explicit_threshold", models.FloatField(default=0.5)),
                (
                    "psycho_pass",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="psychopass.communitypsychopass",
                    ),
                ),
            ],
            options={
                "verbose_name": "Member Dominator",
                "verbose_name_plural": "Member Dominators",
            },
        ),
    ]
