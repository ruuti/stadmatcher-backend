from events.models import Event, Sport, Arena
from events.serializers import EventSerializer, SportSerializer, CitySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from events.helpers import get_events_cache_key
from django.core.cache import cache

class EventList(APIView):
    """
    List all events.
    """
    def get(self, request, format=None):
        cache_key = get_events_cache_key()
        cache_time = 3600
        result = cache.get(cache_key)
        if not result:
            events = Event.objects.filter(datetime__gt=today_midnight).order_by('datetime')
            serializer = EventSerializer(events, many=True, context={"request": request})
            result = serializer.data
            cache.set(cache_key, result, cache_time)
        return Response(result)

class EventDetail(APIView):
    """
    List single event.
    """
    def get(self, request, pk, format=None):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, many=False, context={"request": request})
        return Response(serializer.data)

class SportList(APIView):
    """
    List all sports.
    """
    def get(self, request, format=None):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True, context={"request": request})
        return Response(serializer.data)

class CityList(APIView):
    """
    List all cities.
    """
    def get(self, request, format=None):
        cache_key = 'cities'
        cache_time = 3600
        result = cache.get(cache_key)
        if not result:
            cities = Arena.objects.values('city').distinct().order_by('city')
            serializer = CitySerializer(cities, many=True, context={"request": request})
            result = serializer.data
            cache.set(cache_key, result, cache_time)
        return Response(result)