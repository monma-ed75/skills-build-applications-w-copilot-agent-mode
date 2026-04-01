from django.contrib import admin
from .models import TrackerUser, Team, Activity, LeaderboardEntry, Workout


@admin.register(TrackerUser)
class TrackerUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'team')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'timestamp')


@admin.register(LeaderboardEntry)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
