from django.db import models

import datetime
from django.utils import timezone


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         abstract = True


class Books(models.Model):
    book_catagory = models.CharField(max_length=300)
    book_title = models.CharField(max_length=300)
    book_author_name = models.CharField(max_length=300)
    book_author_profession = models.CharField(max_length=300)
    book_cover_image = models.ImageField(upload_to='images')
    book_upload = models.FileField(upload_to='documents')
    book_overview = models.TextField(max_length=400)
    book_is_front_page = models.BooleanField()
    book_is_published = models.BooleanField()
    publish = models.DateTimeField(default=datetime.datetime.now)
    hits = models.IntegerField(default=0)

    class Meta:
        ordering = ['-publish']

    def __unicode__(self):
        return self.book_title


class Subscriber(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email















