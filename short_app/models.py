from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from hashids import Hashids
from rest_framework.authtoken.models import Token


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


@receiver(pre_save, sender='short_app.Bookmark')
def create_hash_id(**kwargs):
    instance = kwargs.get("instance")
    if instance:
        instance.hash_id = Hashids(salt="yabbadabbadooo").encode(id(instance.url))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
