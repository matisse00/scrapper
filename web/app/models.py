from __future__ import unicode_literals

from django.db import models


class Main(models.Model):
    text = models.TextField()
    author = models.TextField()

