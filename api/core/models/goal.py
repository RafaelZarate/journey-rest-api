
# from django.db import models
# from core.settings import GOAL_TYPE_CHOICES, GOAL_STATUS_CHOICES

# class Goal(models.Model):
#     journey = models.ForeignKey('core.Journey', related_name='goals', on_delete=models.PROTECT)
#     title = models.CharField(max_length=128, default='My Goal')
#     status = models.IntegerField(choices=GOAL_STATUS_CHOICES)
#     due_date = models.DateTimeField(null=True, blank=True)
#     # created_at = models.DateTimeField(auto_now_add=True, null=True)
#     # updated_at = models.DateTimeField(auto_nJow=True)

#     # def save(self, *args, **kwargs):
#     #     self.type = models.IntegerField(choices=GOAL_TYPE_CHOICES[self.journey.type])
#     #     super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.id}"
