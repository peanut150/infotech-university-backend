# Generated by Django 4.2 on 2023-04-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_schedule_daytimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='max_slots',
            field=models.IntegerField(default=50),
        ),
    ]