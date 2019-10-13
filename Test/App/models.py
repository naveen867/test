# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WordFrequency(models.Model):
	word = models.CharField(max_length=2000, unique=True)
	frequency = models.IntegerField(default=0)

	def __unicode__(self):
		return self.word


