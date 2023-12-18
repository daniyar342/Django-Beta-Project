from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Events, Public
from .serializer import EventSerializer, PublicSerializer


class BlogEventsView(mixins.ListModelMixin, GenericViewSet):

    queryset = Events.objects.all()
    serializer_class = EventSerializer


class PublicBlogView(mixins.ListModelMixin, GenericViewSet):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer

