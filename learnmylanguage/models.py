from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class Player(models.Model):
    language = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    email = models.CharField(default=None, max_length=256)
    goal = models.IntegerField(default=20)
    streak = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='"lml_player"'
    def __str__(self):
        return self.username

class Game(models.Model):
    game_hash = models.CharField(max_length=256)
    player1 = models.ForeignKey(Player, models.PROTECT, related_name='player1')
    player2 = models.ForeignKey(Player, models.PROTECT, related_name='player2')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='"lml_game"'
    def __str__(self):
        return self.game_hash


class Snapshot(models.Model):
    player1 = JSONField()
    player2 = JSONField()
    game = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='"lml_snapshot"'
    def __str__(self):
        return self.game
