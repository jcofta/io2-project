from django.test import TestCase

# Create your tests here.
from eleague.models import Tournament
from django.contrib.auth import models as auth_models
from eleague.models import Event
from datetime import datetime


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


class EventTestCase(TestCase):
    def setUp(self):
        user_test = auth_models.User.objects.create(username="Maciej");
        tourna = Tournament.objects.create(tag="testowy_turniej", name="Turniej_testowy", owner=user_test, sport="BAD")
        Event.objects.create(tournament=tourna, date="2017-05-02 10:55:00+00:00", place="Poznan")

    def test_get_date(self):
        tour_test = Event.objects.get(date="2017-05-02 10:55:00+00:00")
        self.assertEqual(tour_test.get_date(),'2017-05-02 10:55:00+00:00')

    def test_get_place(self):
        tour_test = Event.objects.get(date="2017-05-02 10:55:00+00:00")
        self.assertEqual(tour_test.get_place(), 'Poznan')
