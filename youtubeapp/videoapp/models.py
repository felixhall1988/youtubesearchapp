from __future__ import unicode_literals
from django.db import models

from .api import enable_search_specific_channel

class Channel(models.Model):
    channelId = models.TextField(unique=True)
    user = models.TextField(unique=True, null=True)
    title = models.TextField(default='', db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False, db_index=True)
    thumbnail = models.TextField(default='')
uploads_playlist = models.TextField(default='')

class Video(models.Model):
    youtubeid = models.TextField(unique=True)
    uploader = models.ForeignKey(
        Channel, related_name='videos', on_delete=models.CASCADE)
    title = models.TextField(default='')
    duration = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0, null=True)
    favorite_count = models.IntegerField(default=0, null=True)
    uploaded = models.DateTimeField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    description = models.TextField(default='')