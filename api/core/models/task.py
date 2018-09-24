
from django.db import models
from core.settings import TASK_TYPE_CHOICES, TASK_STATUS_CHOICES

class Task(models.Model):
    journey = models.ForeignKey('core.Journey', related_name='tasks', on_delete=models.PROTECT)
    title = models.CharField(max_length=128, default='My Task')
    status = models.IntegerField(choices=TASK_STATUS_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at = models.DateTimeField(auto_nJow=True)

    # def save(self, *args, **kwargs):
    #     self.type = models.IntegerField(choices=GOAL_TYPE_CHOICES[self.journey.type])
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"
