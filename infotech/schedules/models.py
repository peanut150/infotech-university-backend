from django.db import models
from django.utils.timezone import now

# Create your models here.


class Schedule(models.Model):
    name = models.TextField()
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    year_level = models.TextField()
    semester = models.TextField()
    students_assigned = models.ManyToManyField(
        'students.Student', related_name='StudentSchedule_student_assigned', through='schedules.StudentSchedule')
    professor = models.OneToOneField(
        'professors.Professor', related_name='Professor_full_name', on_delete=models.CASCADE)

    daytimes = models.ForeignKey(
        'daytimes.DayTime', related_name='DayTime_full_name', on_delete=models.CASCADE, null=True)

    date_created = models.DateTimeField(default=now, editable=False)
    max_slots = models.IntegerField(default=50)

    def save(self, *args, **kwargs):
        self.name = f"{self.subject} : {self.professor} - {self.daytimes}"
        self.year_level = self.subject.year_level
        self.semester = self.subject.semester
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class StudentSchedule(models.Model):
    schedule = models.ForeignKey(
        'schedules.Schedule', on_delete=models.CASCADE)
    student_assigned = models.ForeignKey(
        'students.Student', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.schedule
