from django.db import models
# Create your models here.


class Student(models.Model):

    class YearLevels(models.TextChoices):
        FIRST_YEAR = '1st Year'
        SECOND_YEAR = '2nd Year'
        THIRD_YEAR = '3rd Year'
        FOURTH_YEAR = 'IU-Y4', '4th Year'

    class Semesters(models.TextChoices):
        FIRST_SEM = '1st Semester'
        SECOND_SEM = '2nd Semester'

    class SexChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=120)
    #
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SexChoices.choices)
    birthdate = models.DateField()
    #
    address = models.CharField(max_length=150)
    birthplace = models.CharField(max_length=150)
    #
    mother_name = models.CharField(max_length=80)
    father_name = models.CharField(max_length=80)
    #
    registrar_done = models.BooleanField()
    clearance_done = models.BooleanField()
    pta_done = models.BooleanField()
    #
    schedules = models.ManyToManyField(
        'schedules.Schedule',  related_name='StudentSchedule_subject', through='schedules.StudentSchedule')
    #
    year_level = models.CharField(max_length=20, choices=YearLevels.choices)
    current_semester = models.CharField(
        max_length=20, choices=Semesters.choices, default=Semesters.FIRST_SEM)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
