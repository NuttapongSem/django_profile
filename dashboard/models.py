from django.db import models


# Create your models here.
class Skill(models.Model):
    name_skill = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_skill
