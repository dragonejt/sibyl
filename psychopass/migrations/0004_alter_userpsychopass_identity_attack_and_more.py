# Generated by Django 5.0 on 2023-12-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("psychopass", "0003_remove_communitypsychopass_community_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpsychopass",
            name="identity_attack",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="insult",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="messages",
            field=models.PositiveIntegerField(db_default=models.Value(0)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="profanity",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="psycho_hazard",
            field=models.BooleanField(db_default=models.Value(False)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="severe_toxicity",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="sexually_explicit",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="threat",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
        migrations.AlterField(
            model_name="userpsychopass",
            name="toxicity",
            field=models.FloatField(db_default=models.Value(0.5)),
        ),
    ]
