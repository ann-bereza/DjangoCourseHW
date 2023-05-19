from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    bio = models.TextField()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    FEEDBACK_TYPE_CHOICES = (
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    )

    image = models.ImageField(upload_to='lesson5/static/img/feedback_images')
    email = models.EmailField()
    description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email
