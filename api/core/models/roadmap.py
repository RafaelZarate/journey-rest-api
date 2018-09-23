from django.db import models
from core.models import User

class RoadMap(models.Model):
    title = models.CharField(max_length=128, default='My Roadmap')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
