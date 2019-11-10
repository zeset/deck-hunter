# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Match, Player, InGameCard, InGameDeck 
# Register your models here.

admin.site.register(Match)
admin.site.register(Player)
admin.site.register(InGameDeck)
admin.site.register(InGameCard)
