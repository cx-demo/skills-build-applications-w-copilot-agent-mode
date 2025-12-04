from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Test', duration=10, date='2025-12-04')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=42)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')
    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
    def test_workout(self):
        self.assertEqual(self.workout.difficulty, 'Easy')
    def test_activity(self):
        self.assertEqual(self.activity.duration, 10)
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 42)
