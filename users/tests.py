from django.test import TestCase

from users.models import User
from django.contrib.auth import models as auth_models

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Patryk", surname="Szymanski", email="p@patryk-szymanski.pl",password="haslo")

    def test_get_name(self):
        user_test = User.objects.get(name="Patryk");
        self.assertEqual(user_test.show_name(), 'This is Patryk')
    def test_get_surname(self):
        user_test = User.objects.get(name="Patryk");
        self.assertEqual(user_test.get_surname(), 'Szymanski')
    def test_get_email(self):
        user_test = User.objects.get(name="Patryk");
        self.assertEqual(user_test.get_email(), 'p@patryk-szymanski.pl')
    def test_get_password(self):
        user_test = User.objects.get(name="Patryk");
        self.assertEqual(user_test.get_password(), 'haslo')
