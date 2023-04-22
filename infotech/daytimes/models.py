from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
# Create your models here.


class DayTime(models.Model):
    class Days(models.TextChoices):
        Monday = 'Monday'
        Tuesday = 'Tuesday'
        Wednesday = 'Wednesday'
        Thursday = 'Thursday'
        Friday = 'Friday'
        Saturday = 'Saturday'
        Sunday = 'Sunday'

    name = models.TextField()
    day = models.TextField(choices=Days.choices)
    time_start = models.TimeField(max_length=40)
    time_end = models.TimeField(max_length=20)

    def save(self, *args, **kwargs):
        self.name = f"{self.day} : {self.time_start} - {self.time_end}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
