# Generated by Django 4.1.7 on 2023-04-21 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0001_initial"),
        ("dominator", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memberdominator",
            name="psycho_pass",
        ),
        migrations.RemoveField(
            model_name="messagedominator",
            name="psycho_pass",
        ),
        migrations.AddField(
            model_name="memberdominator",
            name="community",
            field=models.OneToOneField(
                default=1063590532711972945,
                on_delete=django.db.models.deletion.CASCADE,
                to="community.community",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="messagedominator",
            name="community",
            field=models.OneToOneField(
                default=1063590532711972945,
                on_delete=django.db.models.deletion.CASCADE,
                to="community.community",
            ),
            preserve_default=False,
        ),
    ]
