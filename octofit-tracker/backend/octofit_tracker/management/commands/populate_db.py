from django.core.management.base import BaseCommand
from tracker.models import TrackerUser, Team, Activity, LeaderboardEntry, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        TrackerUser.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        self.stdout.write('Creating users...')
        users = [
            {'email': 'tony@stark.com', 'name': 'Iron Man', 'team': marvel},
            {'email': 'steve@rogers.com', 'name': 'Captain America', 'team': marvel},
            {'email': 'bruce@wayne.com', 'name': 'Batman', 'team': dc},
            {'email': 'clark@kent.com', 'name': 'Superman', 'team': dc},
        ]

        created = []
        for u in users:
            created.append(TrackerUser.objects.create(email=u['email'], name=u['name'], team=u['team']))

        self.stdout.write('Creating activities, leaderboard entries, and workouts...')
        for user in created:
            Activity.objects.create(user=user, activity_type='run', duration_minutes=30)
            LeaderboardEntry.objects.create(user=user, score=100)
            Workout.objects.create(user=user, title='Morning Routine', description='Sample workout')

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
