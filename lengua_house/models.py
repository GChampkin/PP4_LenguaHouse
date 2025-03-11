from django.db import models


class TutorSchedule(models.Model):
    tutor_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    booked_by = models.CharField(max_length=100, blank=True, null=True)
    booked_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"{self.tutor.name} - {self.date} {self.time} ({status})"