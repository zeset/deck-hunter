# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


INGAME = 'In Game'
FINISHED = 'Finished'

GAMESTATES = {
	(INGAME, 'In Game'),
	(FINISHED, 'Finished'),
}


class Player(models.Model):
	username = models.CharField(max_length=20)
	hp = models.IntegerField()
	mp = models.IntegerField()


class Match(models.Model):
	state = models.CharField(max_length=20, choices=GAMESTATES)
	winner = models.ManyToManyField(Player, related_name='wins')
	opponents = models.ManyToManyField(Player, related_name='matches')

	def logMatch():
		pass


class Metahunter(models.Model):
	inGame = models.BooleanField()
	username = models.CharField(max_length=20)


class Deck(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	matches_played = models.IntegerField()
	matches_won = models.IntegerField()
	deckstring = models.CharField(max_length=100)
	deckOrigins = models.CharField(max_length=50)


class Card(models.Model):
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=100)
	origin = models.CharField(max_length=50)
	effectGenerated = models.BooleanField(default=False)
	flavourText = models.CharField(max_length=200)


class InGameDeck(models.Model):
	ncards = models.IntegerField()


class InGameCard(models.Model):
	modified = models.BooleanField(default=False)
	silenced = models.BooleanField(default=False)
	mana_buff = models.IntegerField()
	attack_buff = models.IntegerField()
	health_buff = models.IntegerField()


	def burnCard():
		pass
