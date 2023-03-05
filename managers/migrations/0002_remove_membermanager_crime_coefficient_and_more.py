# Generated by Django 4.1.7 on 2023-03-05 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membermanager',
            name='crime_coefficient',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='discord_notify_role',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='identity_attack',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='insult',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='profanity',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='severe_toxicity',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='sexually_explicit',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='threat',
        ),
        migrations.RemoveField(
            model_name='membermanager',
            name='toxicity',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='crime_coefficient',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='discord_notify_role',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='identity_attack',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='insult',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='profanity',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='severe_toxicity',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='sexually_explicit',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='threat',
        ),
        migrations.RemoveField(
            model_name='messagemanager',
            name='toxicity',
        ),
        migrations.AddField(
            model_name='membermanager',
            name='crime_coefficient_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='crime_coefficient_trigger',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='discord_notify_target',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='identity_attack_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='insult_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='profanity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='severe_toxicity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='sexually_explicit_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='threat_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='membermanager',
            name='toxicity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='crime_coefficient_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='crime_coefficient_trigger',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='discord_notify_target',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='identity_attack_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='insult_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='profanity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='severe_toxicity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='sexually_explicit_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='threat_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Null'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AddField(
            model_name='messagemanager',
            name='toxicity_trigger',
            field=models.FloatField(default=0.5),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='discord_log_channel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='discord_log_channel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]