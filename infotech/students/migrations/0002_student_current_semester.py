# Generated by Django 4.1.7 on 2023-03-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_semester',
            field=models.CharField(choices=[('Sem-1', '1st Semester'), ('Sem-2', '2nd Semester')], default='Sem-1', max_length=20),
        ),
    ]