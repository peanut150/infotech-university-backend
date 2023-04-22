# Generated by Django 4.2 on 2023-04-22 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
            ],
        ),
    ]
