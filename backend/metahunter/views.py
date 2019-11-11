# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from .models import Metahunter, Deck, Card
from .serializers import MetahunterSerializer, DeckSerializer, CardSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class MetahunterViewSet(viewsets.ModelViewSet):
	serializer_class = MetahunterSerializer
	queryset = Metahunter.objects.all()


class DeckViewSet(viewsets.ModelViewSet):
	serializer_class = DeckSerializer
	queryset = Deck.objects.all()


class CardViewSet(viewsets.ModelViewSet):
	serializer_class = CardSerializer
	queryset = Card.objects.all()