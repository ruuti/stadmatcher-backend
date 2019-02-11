from django.db import models
from django.core.cache import cache
import uuid
import os
from events.helpers import get_events_cache_key
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join(filename)

class Arena(models.Model):
	title = models.CharField(max_length=250, null=False)
	city = models.CharField(max_length=250, null=False)
	
	def __str__(self):
		return self.title

class Sport(models.Model):
	title = models.CharField(max_length=250, null=False)
	
	def __str__(self):
		return self.title

class League(models.Model):
	title = models.CharField(max_length=250, null=False)
	sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False, related_name='sport')
	
	def __str__(self):
		return self.title

class Team(models.Model):
	title = models.CharField(max_length=250, null=False)
	league = models.ForeignKey(League, on_delete=models.CASCADE, null=False, related_name='league')
	logo = models.ImageField(upload_to=get_file_path, null=True)

	def __str__(self):
		return self.title

class Event(models.Model):

	home_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='home_team')
	away_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='away_team')
	arena = models.ForeignKey(Arena, on_delete=models.CASCADE, null=False, related_name='arena') 
	datetime = models.DateTimeField(db_index=True, null=False)
	created_at = models.DateTimeField(auto_now_add=True,db_index=True, null=False)
	updated_at = models.DateTimeField(auto_now=True,db_index=True, null=False)
	friendly = models.BooleanField(default=False)

@receiver(post_save, sender=Event, dispatch_uid="clear_cache_handle")
@receiver(post_save, sender=Team, dispatch_uid="clear_cache_handle")
@receiver(post_save, sender=League, dispatch_uid="clear_cache_handle")
@receiver(post_save, sender=Sport, dispatch_uid="clear_cache_handle")
@receiver(post_save, sender=Arena, dispatch_uid="clear_cache_handle")
@receiver(post_delete, sender=Event, dispatch_uid="clear_cache_handle")
@receiver(post_delete, sender=Team, dispatch_uid="clear_cache_handle")
@receiver(post_delete, sender=League, dispatch_uid="clear_cache_handle")
@receiver(post_delete, sender=Sport, dispatch_uid="clear_cache_handle")
@receiver(post_delete, sender=Arena, dispatch_uid="clear_cache_handle")
def clear_cache_handle(sender, instance, **kwargs):
	"""
	Delete cache automatically when data changes
	"""
	events_cache_key = get_events_cache_key()
	cache.delete_many(['cities', events_cache_key])