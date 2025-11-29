from django.core.management.base import BaseCommand
from octofit_tracker.mongo_models import User, Team, Activity, Workout, Leaderboard
from mongoengine import get_db
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = get_db()
        # Törlés
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Workout.objects.delete()
        Leaderboard.objects.delete()
        # Index létrehozása email-re
        db['users'].create_index('email', unique=True)

        # Csapatok
        marvel = Team(name='Marvel').save()
        dc = Team(name='DC').save()
        # Felhasználók
        ironman = User(name='Iron Man', email='ironman@marvel.com', team=marvel).save()
        captain = User(name='Captain America', email='cap@marvel.com', team=marvel).save()
        superman = User(name='Superman', email='superman@dc.com', team=dc).save()
        batman = User(name='Batman', email='batman@dc.com', team=dc).save()
        # Aktivitások
        Activity(user=ironman, type='run', duration=30, date=date(2025, 11, 1)).save()
        Activity(user=captain, type='cycle', duration=45, date=date(2025, 11, 2)).save()
        Activity(user=superman, type='swim', duration=60, date=date(2025, 11, 3)).save()
        Activity(user=batman, type='run', duration=25, date=date(2025, 11, 4)).save()
        # Edzések
        Workout(name='Pushups', description='Do 20 pushups', difficulty='easy').save()
        Workout(name='Plank', description='Hold plank for 1 min', difficulty='medium').save()
        # Leaderboard
        Leaderboard(user=ironman, score=100).save()
        Leaderboard(user=superman, score=120).save()
        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
