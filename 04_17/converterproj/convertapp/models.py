from django.db import models

class TimerHistory(models.Model):
    duration = models.IntegerField(help_text="Duration in seconds")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.duration} seconds at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
