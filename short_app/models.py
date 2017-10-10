from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids
from django.db.models.signals import pre_save

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


@receiver(post_save, sender='short_app.Bookmark')
def create_hash_id(**kwargs):
    instance = kwargs.get("instance")
    if kwargs.get("created"):
        instance.hash_id = Hashids(salt="yabbadabbadooo").encode(id(instance.url))
        instance.save()
