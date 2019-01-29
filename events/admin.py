# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Team, League, Sport, Event, Arena

class ArenaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')
admin.site.register(Arena, ArenaAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team, TeamAdmin)

class LeagueAdmin(admin.ModelAdmin):
    pass
admin.site.register(League, LeagueAdmin)

class SportAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sport, SportAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'home_team', 'away_team', 'arena', 'datetime')
admin.site.register(Event, EventAdmin)