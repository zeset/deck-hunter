# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from metagame.models import Player, Match, InGameDeck, InGameCard

FRELJORD = 'Freljord'
DEMACIA = 'Demacia'
NOXUS = 'Noxus'
IONIA = 'Ionia'
LASISLASOSCURAS = 'Las Islas Oscuras'
PILTOVER = 'Piltover'
ZAUN = 'Zaun'

ORIGINS = {
	(FRELJORD, 'freljord'),
	(DEMACIA, 'demacia'),
	(NOXUS, 'noxus'),
	(IONIA, 'ionia'),
	(LASISLASOSCURAS, 'las_islas_oscuras'),
	(PILTOVER, 'piltover'),
	(ZAUN, 'zaun'),
}


class Metahunter(models.Model):
	inGame = models.BooleanField()
	username = models.CharField(max_length=20)

	def __str__(self):
		return self.username


class Deck(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	matches_played = models.IntegerField()
	matches_won = models.IntegerField()
	deckstring = models.CharField(max_length=100)
	deckOrigin1 = models.CharField(max_length=50, choices=ORIGINS)
	deckOrigin2 = models.CharField(max_length=50, choices=ORIGINS)

	def __str__(self):
		return f"{self.name} - {self.matches_played}/{self.matches_won}" 


class Card(models.Model):
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=100)
	origin = models.CharField(max_length=50, choices=ORIGINS)
	effectGenerated = models.BooleanField(default=False)
	flavourText = models.CharField(max_length=200)