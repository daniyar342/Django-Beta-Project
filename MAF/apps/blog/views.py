from django.shortcuts import render
from rest_framework import generics
from .models import Events
from .serializer import EventSerializer
class BlogEvents(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
