from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.author

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    logo = models.FileField()

    def __str__(self):
        return self.title

