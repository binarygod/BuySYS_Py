from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EveUser(AbstractUser):
    character_id = models.IntegerField(null=True)
    corporation_id = models.IntegerField(null=True)
    alliance_id = models.IntegerField(null=True)