from django.db import models

class RoadMap(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128, default='My Roadmap')
    due_date = models.DateTimeField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
