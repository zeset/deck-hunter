from rest_framework import serializers
from .models import Metahunter, Card, Deck


class MetahunterSerializer(serializers.Serializer):
    class Meta:
        model = Metahunter
        fields = '__all__'

class CardSerializer(serializers.Serializer):
    class Meta:
        model = Card
        fields = '__all__'

class DeckSerializer(serializers.Serializer):
    class Meta:
        model = Deck
        fields = '__all__'