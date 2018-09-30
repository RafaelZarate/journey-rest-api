
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True)
    email_address = models.EmailField()
    dob = models.DateField(max_length=8)
    country_code = models.IntegerField(default=52)
    is_admin = models.BooleanField(default=False)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name.strip()} {self.last_name.strip()}".title()

    def __str__(self):
        return f"{self.id}"

