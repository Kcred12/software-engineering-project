from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_LOW = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_HIGH = 3
    PRIORITY_CRITICAL = 4
    PRIORITY_CHOICES = [
    (PRIORITY_LOW, 'Low'),
    (PRIORITY_MEDIUM, 'Medium'),
    (PRIORITY_HIGH, 'High'),
    (PRIORITY_CRITICAL, 'Critical'),
]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM, )
    due_date = models.DateTimeField(default=None)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['due_date', '-priority']  # default ordering; you can override in views
        indexes = [
            models.Index(fields=['due_date']),
        ]

    def __str__(self):
        return self.title

    def is_overdue(self):
        return bool(self.due_date and (self.due_date < timezone.now()) and not self.completed)