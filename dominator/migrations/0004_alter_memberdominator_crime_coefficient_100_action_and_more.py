# Generated by Django 4.2.6 on 2023-10-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominator', '0003_remove_memberdominator_discord_log_channel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberdominator',
            name='crime_coefficient_100_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='crime_coefficient_300_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=4),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='memberdominator',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
        migrations.AlterField(
            model_name='messagedominator',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Notify'), (1, 'Remove'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=0),
        ),
    ]
