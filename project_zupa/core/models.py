from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os

from django_google_maps import fields as map_fields

# Create your models here.
class Glasnik(models.Model):
    naziv = models.CharField(max_length=100)
    broj = models.IntegerField()
    slika = models.ImageField(max_length=None)
    datoteka = models.FileField(max_length=100)
    blog_views=models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Glasnici'
        ordering = ["-broj"]


    def __str__(self):
        return self.naziv + str(self.broj)

    def slug(self):
        return slugify(self.naziv + self.broj)

    def filename(self): 
        return os.path.basename(self.file.naziv)


class Post(models.Model):
    title = models.CharField(max_length=100, unique= True)
    slika = models.ImageField(max_length=None, default=None)
    sadrzaj = models.TextField(default=None)
    slug = models.SlugField(blank=True, null=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vijesti'

    def __str__(self):
        return self.title

    @property
    def views_count(self):
        return PostViews.objects.filter(post=self).count()



class PostViews(models.Model):
    IPAddres= models.GenericIPAddressField(default="45.243.82.169")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} in {1} post'.format(self.IPAddres,self.post.title)


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


class Poruka(models.Model):
    name =  models.CharField(max_length=100)
    email  = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
