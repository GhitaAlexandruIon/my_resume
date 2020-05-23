from django.db import models
from ckeditor.fields import RichTextField


class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    programing_languages = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
