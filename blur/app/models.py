from django.db import models


# Create your models here.
from django.utils import timezone


class Video(models.Model):
    RUNNING = 'running'
    PENDING = 'pending'
    FINISHED = 'finished'
    FAILED = 'failed'
    STATUS_CHOICES = (
        (RUNNING, 'Running'),
        (PENDING, 'pending'),
        (FINISHED, 'finished'),
        (FAILED, 'failed'),
    )
    link = models.TextField(null=False)
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=10)
    result = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
