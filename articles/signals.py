from django.db.models.signals import pre_save, post_save
from .models import Article


def article_pre_save(*args, **kwargs):
    print("pre_save")
    print(args, kwargs)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(*args, **kwargs):
    print("post_save")
    print(args, kwargs)


post_save.connect(article_post_save, sender=Article)
