# Generated by Django 4.1.7 on 2023-04-21 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dominator", "0002_remove_memberdominator_psycho_pass_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memberdominator",
            name="discord_log_channel",
        ),
        migrations.RemoveField(
            model_name="memberdominator",
            name="discord_notify_target",
        ),
        migrations.RemoveField(
            model_name="messagedominator",
            name="discord_log_channel",
        ),
        migrations.RemoveField(
            model_name="messagedominator",
            name="discord_notify_target",
        ),
    ]
