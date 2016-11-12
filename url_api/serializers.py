from rest_framework import serializers
from short_app.models import Click, Bookmark


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ['link', 'time_click']


class BookmarkSerilizer(serializers.ModelSerializer):
    short_link = serializers.HyperlinkedIdentityField(view_name='forward_view', lookup_field='hash_id')

    class Meta:
        model = Bookmark
        fields = ['id',
                  'title',
                  'description',
                  'short_link',
                  'url',
                  'created',
                  'count',
                  'user']
