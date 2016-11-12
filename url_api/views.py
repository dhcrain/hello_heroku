# from django.shortcuts import render
from rest_framework import generics
from short_app.models import Click, Bookmark
from url_api.serializers import ClickSerializer, BookmarkSerilizer
from datetime import datetime, date, timedelta
# import calendar


class ClickAPIView(generics.ListAPIView):
    # model = Click
    serializer_class = ClickSerializer

    def get_queryset(self):
        one_month = datetime.now() + timedelta(days=-30)
        click = Click.objects.filter(time_click__gt=one_month)
        # print(one_month)
        for url in click:
            print(url.link.pk)  # pk of all clicks
            date = url.time_click.strftime("%Y-%m-%d")  # str of yr-m-d
            print(date)
            # Goal: for each url.link.pk gather the num of clicks for each date

    def get_month_range():
        start_date = date.today()
        # print(start_date)
        end_date = start_date + timedelta(days=-30)
        return (start_date, end_date)

    a_day = timedelta(days=1)
    first_day, end_date = get_month_range()
    while first_day > end_date:
        # print(first_day)  # list of days for 30 days previous to today
        first_day -= a_day


class LinkAPIView(generics.ListAPIView):
    model = Bookmark
    serializer_class = BookmarkSerilizer

    def get_queryset(self):
        return Bookmark.objects.all()

# from django.http import HttpResponse
# import json
# from django.views.generic import View

# def unzip_data(data):
#     return [[node[_] for node in data] for _ in range(len(data[0]))]
#
#
# class GraphView(View):
#
#     def get(self, request):
#         livetvusername = request.user.userprofile.livetvusername
#         dataX, dataY, siteY = unzip_data(Click.objects.get_plottable_eight_minutes(livetvusername))
#         last_node = Click.objects.filter(livetvusername=livetvusername).last()
#         current_count = 0
#         if last_node:
#             current_count = last_node.current_total
#         context = {"frontpaged": request.user.userprofile.frontpaged,
#                    "maxY": max(dataY),
#                    "maxSiteY": max(siteY),
#                    "dataX": dataX,
#                    "dataY": dataY,
#                    "siteY": siteY,
#                    "current_count": current_count}
#         return HttpResponse(json.dumps(context), content_type="application/json")
