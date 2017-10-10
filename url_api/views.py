from django.contrib.auth import get_user_model
from url_api.serializers import ClickSerializer, BookmarkSterilizer, UserSerializer
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from short_app.models import Click, Bookmark


class ClickAPIView(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class ClickRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSterilizer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSterilizer


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
