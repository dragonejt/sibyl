# Generated by Django 4.1.7 on 2023-03-12 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominator', '0003_alter_memberdominator_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberdominator',
            old_name='identity_attack_trigger',
            new_name='identity_attack_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='insult_trigger',
            new_name='insult_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='profanity_trigger',
            new_name='profanity_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='severe_toxicity_trigger',
            new_name='severe_toxicity_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='sexually_explicit_trigger',
            new_name='sexually_explicit_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='threat_trigger',
            new_name='threat_threshold',
        ),
        migrations.RenameField(
            model_name='memberdominator',
            old_name='toxicity_trigger',
            new_name='toxicity_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='identity_attack_trigger',
            new_name='identity_attack_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='insult_trigger',
            new_name='insult_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='profanity_trigger',
            new_name='profanity_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='severe_toxicity_trigger',
            new_name='severe_toxicity_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='sexually_explicit_trigger',
            new_name='sexually_explicit_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='threat_trigger',
            new_name='threat_threshold',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='toxicity_trigger',
            new_name='toxicity_threshold',
        ),
    ]