from rest_framework import serializers
from events.models import Event, Team, Arena, Sport, League
from backend import settings

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('title', 'id',)

class LeagueSerializer(serializers.ModelSerializer):
    sport = SportSerializer(many=False, read_only=True)
    class Meta:
        model = League
        fields = ('title', 'sport',)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Arena
        fields = ('city',)

class ArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arena
        fields = ('title', 'city')

class TeamSerializer(serializers.ModelSerializer):
    league = LeagueSerializer(many=False, read_only=True)
    logo = serializers.SerializerMethodField('get_logo_url')
    class Meta:
        model = Team
        fields = ('title', 'logo', 'league',)
    def get_logo_url(self, obj):
        full_url = None
        if(obj.logo):
            full_url = settings.BASE_URL+settings.MEDIA_URL+str(obj.logo)
        return full_url

class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    home_team = TeamSerializer(many=False, read_only=True)
    away_team = TeamSerializer(many=False, read_only=True)
    arena = ArenaSerializer(many=False, read_only=True)
    datetime = serializers.DateTimeField()

    class Meta:
        model = Event