from django.db import models

LESSON_TIMES = [
    ("09:00:00", "09:00 AM"),
    ("10:00:00", "10:00 AM"),
    ("11:00:00", "11:00 AM"),
    ("14:00:00", "02:00 AM"),
    ("15:00:00", "03:00 AM"),
    ("16:00:00", "04:00 AM"),
]


class TutorSchedule(models.Model):
    tutor_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=LESSON_TIMES)
    is_booked = models.BooleanField(default=False)
    booked_by = models.CharField(max_length=100, blank=True, null=True)
    booked_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"{self.tutor.name} - {self.date} {self.get_time_display()} ({status})"
