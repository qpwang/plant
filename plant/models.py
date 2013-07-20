# -*- coding: utf-8 -*-
from django.db import models


class Plant(models.Model):
    class Meta:
        db_table = 'plant'
        verbose_name = verbose_name_plural = u'植物'
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    birthdate = models.DateField()
    temperature = models.CharField(max_length=100)
    humidty = models.CharField(max_length=100)
    sensor_id = models.CharField(max_length=100)



