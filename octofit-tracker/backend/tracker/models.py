from django.db import models


class TrackerUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(TrackerUser, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(TrackerUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    user = models.ForeignKey(TrackerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'workouts'
