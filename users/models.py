from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def show_name(self):
        return "This is " + self.name

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password