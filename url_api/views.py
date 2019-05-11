from datetime import datetime

from django.contrib.auth import get_user_model
from django_filters import filters
from rest_framework import permissions, generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from short_app.models import Click, Bookmark
from url_api.serializers import ClickSerializer, BookmarkLinkSerializer, BookmarkSerializer, UserSerializer


class ClickAPIView(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class ClickRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class LinkUrlRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookmarkLinkSerializer

    def get_object(self):
        hash_id = self.kwargs.get('hash_id', None)
        if hash_id is not None:
            try:
                link = Bookmark.objects.get(hash_id=hash_id)
                Click.objects.create(link=link, time_click=datetime.now())
            except:
                raise NotFound(detail="Error 404, url not found", code=404)
            return link


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
