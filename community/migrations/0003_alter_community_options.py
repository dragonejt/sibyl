# Generated by Django 4.1.7 on 2023-04-21 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0002_community_discord_log_channel_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="community",
            options={"verbose_name": "Community", "verbose_name_plural": "Communities"},
        ),
    ]
