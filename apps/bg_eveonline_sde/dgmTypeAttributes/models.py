from django.db import models
from apps.bg_eveonline_sde.utils import CustomFloatField


class TypeAttributes(models.Model):
    typeID = models.IntegerField(primary_key=True)
    attributeID = models.IntegerField(null=False)
    valueInt = models.IntegerField(null=True)
    valueFloat = CustomFloatField(null=True)

    class Meta:
        db_table = 'dgmTypeAttributes'
