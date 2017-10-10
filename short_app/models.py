from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    hash_id = models.CharField(max_length=10, null=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    @property
    def count(self):
        link_clicks = Click.objects.filter(link=self)
        return link_clicks.count()


class Click(models.Model):
    link = models.ForeignKey(Bookmark)
    time_click = models.DateTimeField()

    class Meta:
        ordering = ["-time_click"]
