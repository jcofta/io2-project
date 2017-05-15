from django.test import TestCase

# Create your tests here.
from eleague.models import Tournament
from django.contrib.auth import models as auth_models

class TournamentlTestCase(TestCase):
    def setUp(self):
        user_test = auth_models.User.objects.create(username="Wojtek");
        Tournament.objects.create(tag="testowy", name="Turniej testowy", owner=user_test, sport="BAD")

    def test_get_name(self):
        tour_test = Tournament.objects.get(name="Turniej testowy");
        self.assertEqual(tour_test.show_tag(), 'This is testowy Tournament')

    def test_get_sport(self):
        tour_test = Tournament.objects.get(name="Turniej testowy");
        self.assertEqual(tour_test.get_sport(), "BAD")

    def test_all(self):
        tour_test = Tournament.objects.get(name="Turniej testowy");
        self.assertEqual(tour_test.get_all(), "testowy Turniej testowy BAD")

    def test_owner(self):
        tour_test = Tournament.objects.get(name="Turniej testowy");
        self.assertEqual(tour_test.get_owner(), "Wojtek")

    def test_all_with_owner(self):
        tour_test = Tournament.objects.get(name="Turniej testowy");
        self.assertEqual(tour_test.get_all_with_owner(), "testowy Turniej testowy Wojtek BAD")
