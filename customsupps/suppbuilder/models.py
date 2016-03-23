from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class CustomStack(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    caffeine = models.IntegerField(default=0)
    theanine = models.IntegerField( default=0)
    carnitine = models.IntegerField( default=0)
    tyrosine = models.IntegerField( default=0)
    synephrine = models.IntegerField( default=0)
    creatine = models.IntegerField( default=0)
    hmb = models.IntegerField( default=0)
    alpha_gpc = models.IntegerField( default=0)
    betaine = models.IntegerField( default=0)
    beta_alanine = models.IntegerField(default=0)
    citrulline_malate = models.IntegerField( default=0)
    bcaa = models.IntegerField( default=0)
    beet_root = models.IntegerField( default=0)

    def __unicode__(self):
        return self.title