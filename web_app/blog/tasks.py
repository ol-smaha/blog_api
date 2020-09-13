from __future__ import absolute_import, unicode_literals
from celery import task

from .models import Post


@task()
def reset_votes():
    Post.objects.all().update(votes_amount=0)
