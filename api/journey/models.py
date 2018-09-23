from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=255, null=False)
    points = models.IntegerField()

    def __str__(self):
        return "{self.title} - {self.points}"

