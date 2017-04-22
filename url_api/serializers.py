from rest_framework import serializers
from short_app.models import Click, Bookmark
from datetime import date, timedelta
import operator
from django.contrib.auth.models import User


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ['link', 'time_click']


class BookmarkSerilizer(serializers.ModelSerializer):
    short_link = serializers.HyperlinkedIdentityField(view_name='forward_view', lookup_field='hash_id')
    month_stats = serializers.SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_month_stats(self, obj):
        start_date = date.today()
        end_date = start_date + timedelta(days=-30)
        a_day = timedelta(days=1)
        month_dict = {}

        while start_date > end_date:
            month_dict[start_date.strftime("%Y-%m-%d")] = 0
            start_date -= a_day

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

    def get_x_dates(self, obj, unpack_dates_clicks):
        dates = unpack_dates_clicks
        return dates

    def get_y_click_count(self, obj, unpack_dates_clicks):
        clicks = unpack_dates_clicks
        return clicks

    class Meta:
        model = Bookmark
        fields = ['id',
                  'title',
                  'description',
                  'short_link',
                  'url',
                  'created',
                  'count',
                  'user',
                  'month_stats',
                  ]


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
