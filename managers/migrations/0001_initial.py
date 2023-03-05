# Generated by Django 4.1.7 on 2023-03-04 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0008_alter_communityprofile_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_log_channel', models.CharField(max_length=20)),
                ('discord_notify_role', models.CharField(max_length=20)),
                ('crime_coefficient', models.JSONField(default={'action': 'NOTIFY', 'trigger': 100})),
                ('toxicity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('severe_toxicity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('identity_attack', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('insult', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('threat', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('profanity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('sexually_explicit', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.communityprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MemberManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_log_channel', models.CharField(max_length=20)),
                ('discord_notify_role', models.CharField(max_length=20)),
                ('crime_coefficient', models.JSONField(default={'action': 'NOTIFY', 'trigger': 100})),
                ('toxicity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('severe_toxicity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('identity_attack', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('insult', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('threat', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('profanity', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('sexually_explicit', models.JSONField(default={'action': 'NOTIFY', 'trigger': 0.5})),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.communityprofile')),
            ],
        ),
    ]
