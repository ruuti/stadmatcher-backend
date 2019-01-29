# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid
import os

def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join(filename)

class Arena(models.Model):
	title = models.CharField(max_length=250, null=False)
	city = models.CharField(max_length=250, null=False)
	
	def __str__(self):
		return self.title.encode('utf-8')

class Sport(models.Model):
	title = models.CharField(max_length=250, null=False)
	
	def __str__(self):
		return self.title.encode('utf-8')

class League(models.Model):
	title = models.CharField(max_length=250, null=False)
	sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False, related_name='sport')
	
	def __str__(self):
		return self.title.encode('utf-8')

class Team(models.Model):
	title = models.CharField(max_length=250, null=False)
	league = models.ForeignKey(League, on_delete=models.CASCADE, null=False, related_name='league')
	logo = models.ImageField(upload_to=get_file_path, null=True)

	def __str__(self):
		return self.title.encode('utf-8')

class Event(models.Model):

	home_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='home_team')
	away_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='away_team')
	arena = models.ForeignKey(Arena, on_delete=models.CASCADE, null=False, related_name='arena') 
	datetime = models.DateTimeField(db_index=True, null=False)
	created_at = models.DateTimeField(auto_now_add=True,db_index=True, null=False)
	updated_at = models.DateTimeField(auto_now=True,db_index=True, null=False)
	friendly = models.BooleanField(default=False)