# Generated by Django 4.1.7 on 2023-03-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_remove_membermanager_crime_coefficient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membermanager',
            name='crime_coefficient_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='membermanager',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='crime_coefficient_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='identity_attack_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='insult_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='profanity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='severe_toxicity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='sexually_explicit_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='threat_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
        migrations.AlterField(
            model_name='messagemanager',
            name='toxicity_action',
            field=models.IntegerField(choices=[(0, 'Noop'), (1, 'Notify'), (2, 'Mute'), (3, 'Kick'), (4, 'Ban')], default=1),
        ),
    ]