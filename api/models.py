from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    teams = models.ManyToManyField('Team', related_name='team_members', blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Team(models.Model):
    team_name = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='user_teams', blank=True)
