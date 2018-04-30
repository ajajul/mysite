# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Students2(models.Model):
	fname = models.CharField(max_length=120, null=True, blank=True)
	lname = models.CharField(max_length=120, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.fname
