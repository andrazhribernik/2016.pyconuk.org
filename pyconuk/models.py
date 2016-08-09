from django.db import models
from django_amber.models import ModelWithContent, ModelWithoutContent


class Page(ModelWithContent):
    title = models.CharField(max_length=255)
    callout_big_1 = models.CharField(max_length=255)
    callout_big_2 = models.CharField(max_length=255)
    callout_small = models.CharField(max_length=255)
    tito_required = models.BooleanField(default=False)

    dump_dir_path = 'pages'


class NewsItem(ModelWithContent):
    title = models.CharField(max_length=255)
    date = models.DateField()

    dump_dir_path = 'news'


class Redirection(ModelWithoutContent):
    new_url = models.CharField(max_length=255)

    dump_dir_path = 'redirections'
