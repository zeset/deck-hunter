# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Metahunter, Deck, Card

admin.site.register(Metahunter)
admin.site.register(Deck)
admin.site.register(Card)
# Register your models here.
