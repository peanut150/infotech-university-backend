from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
# Create your models here.


class Subject(models.Model):
    class YearLevels(models.TextChoices):
        FIRST_YEAR = '1st Year'
        SECOND_YEAR = '2nd Year'
        THIRD_YEAR = '3rd Year'
        FOURTH_YEAR = '4th Year'

    class Semesters(models.TextChoices):
        FIRST_SEM = '1st Semester'
        SECOND_SEM = '2nd Semester'

    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20)
    year_level = models.CharField(max_length=20, choices=YearLevels.choices)
    semester = models.CharField(
        max_length=20, choices=Semesters.choices, default=Semesters.FIRST_SEM)

    def __str__(self):
        return self.name
