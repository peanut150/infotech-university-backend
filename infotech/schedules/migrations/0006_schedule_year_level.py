# Generated by Django 4.2 on 2023-04-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_schedule_max_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='year_level',
            field=models.TextField(default='Placeholder Year Level'),
            preserve_default=False,
        ),
    ]
