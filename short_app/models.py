from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from short_app.utils import make_short_link


class Bookmark(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    hash_id = models.CharField(max_length=10)
    user = models.ForeignKey(User)

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


@receiver(pre_save, sender=Bookmark)
def create_user_profile(**kwargs):
    instance = kwargs.get("instance")
    instance.hash_id = make_short_link(instance.url)
