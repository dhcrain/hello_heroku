import operator
from datetime import date, timedelta

from django.contrib.auth.models import User
from rest_framework import serializers

from short_app.models import Click, Bookmark


def get_month_dict(start_date = date.today(), end_date = date.today() + timedelta(days=-30)):
    month_dict = {}
    a_day = timedelta(days=1)
    while start_date > end_date:
        month_dict[start_date.strftime("%Y-%m-%d")] = 0
        start_date -= a_day
    return month_dict


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ['link', 'time_click']


class BookmarkLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = ['url']


class BookmarkSerializer(serializers.ModelSerializer):
    short_link = serializers.HyperlinkedIdentityField(view_name='forward_view', lookup_field='hash_id')
    month_stats = serializers.SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_month_stats(self, obj):
        month_dict = get_month_dict()

        for item in obj.click_set.all():
            click_time = item.time_click.strftime("%Y-%m-%d")
            if click_time in month_dict.keys():
                month_dict[click_time] += 1

        sorted_date_click = sorted(month_dict.items(), key=operator.itemgetter(0))
        dates = []
        counts = []
        for calendar, count in sorted_date_click:
            dates.append(calendar)
            counts.append(count)

        return dates, counts

    class Meta:
        model = Bookmark
        fields = ['id',
                  'title',
                  'description',
                  'short_link',
                  'hash_id',
                  'url',
                  'created',
                  'count',
                  'user',
                  'month_stats',
                  ]

    def create(self, validated_data):
        bookmark = Bookmark()
        bookmark.title = validated_data['title']
        bookmark.url = validated_data['url']
        bookmark.user = validated_data['user']
        desc = validated_data.get('description')
        if desc:
            bookmark.description = desc
        bookmark.save()
        return bookmark


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
