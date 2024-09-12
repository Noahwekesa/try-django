from django.db import models
from django.db.models.query import create_namedtuple_class
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()


post_save.connect(article_post_save, sender=Article)
