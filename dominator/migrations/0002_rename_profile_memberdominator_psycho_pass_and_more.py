# Generated by Django 4.1.7 on 2023-03-22 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberdominator',
            old_name='profile',
            new_name='psycho_pass',
        ),
        migrations.RenameField(
            model_name='messagedominator',
            old_name='profile',
            new_name='psycho_pass',
        ),
    ]
