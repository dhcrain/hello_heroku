# from django.shortcuts import render
from django.contrib.auth import get_user_model
from url_api.serializers import ClickSerializer, BookmarkSerilizer, UserSerializer
from rest_framework import permissions, generics
from short_app.models import Click, Bookmark


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


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
