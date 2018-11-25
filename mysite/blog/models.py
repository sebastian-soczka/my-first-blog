from django.db import models
from django.utils import timezone


class Series(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Book(models.Model):

    title = models.CharField(max_length=200)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    volume_nr = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    chapter_nr = models.PositiveIntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
        return self.title


