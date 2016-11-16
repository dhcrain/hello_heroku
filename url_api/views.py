# from django.shortcuts import render
from rest_framework import generics
from short_app.models import Click, Bookmark
from url_api.serializers import ClickSerializer, BookmarkSerilizer


class ClickAPIView(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class ClickRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer

class LinkAPIView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerilizer


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerilizer
