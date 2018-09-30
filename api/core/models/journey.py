
from django.db import models
from core.settings import JOURNEY_TYPE_CHOICES, JOURNEY_STATUS_CHOICES

class Journey(models.Model):
    roadmap = models.ForeignKey('core.RoadMap', related_name='journeys', on_delete=models.PROTECT)
    title = models.CharField(max_length=128, default='My Journey')
    type = models.IntegerField(choices=JOURNEY_TYPE_CHOICES)
    status = models.IntegerField(choices=JOURNEY_STATUS_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
