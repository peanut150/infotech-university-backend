# Generated by Django 4.2 on 2023-04-22 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_enrolled_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrolled_subjects',
        ),
    ]
