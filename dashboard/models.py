from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sites.models import Site

class ResourceMixin(models.Model):
    title  = models.CharField(max_length=100)
    desc  = models.TextField(null=True, blank=True)
    date  = models.DateTimeField(default=timezone.now)
    image  = models.ImageField(upload_to="uploads/images", blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_file_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.file.url
        return f"{domain}{path}"
    
    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.image.url
        return f"{domain}{path}"

class Photo(ResourceMixin):
    file  = models.FileField(upload_to="uploads/photos")

class Preaching(ResourceMixin):
    preacher = models.CharField(max_length=100)
    file   = models.FileField(upload_to="uploads/preachings")

class Video(ResourceMixin):
    file  = models.FileField(upload_to="uploads/videos")

class Material(ResourceMixin):
    file  = models.FileField(upload_to="uploads/materials")

class Leader(models.Model):
    position    = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE) 
    contacts    = models.CharField(max_length=50)
    date        = models.DateTimeField(default=timezone.now)
    inactive    = models.DateTimeField(null=True, blank=True)
    # full_name   = models.CharField(max_length=100)

    # def save(self):
    #     self.full_name = self.user.profile.full_name
    #     super()

    def __str__(self):
        return self.position

    def __unicode__(self):
        return self.position

class ChurchInfo(models.Model):
    about          = models.TextField()
    address        = models.TextField()
    head_pastor    = models.CharField(max_length=100) 
    help_text      = models.TextField()

    class Meta:
        verbose_name_plural = "Church Info"


    def __str__(self):
        return "Church Info"

    def __unicode__(self):
        return "Church Info"


class DailyDevotion(models.Model):
    title       = models.CharField(max_length=100)
    image       = models.ImageField(upload_to="uploads/Devotions")
    description = models.TextField() 
    verse       = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Notification(models.Model):
    title   = models.CharField(max_length=100)
    message = models.TextField()
    date    = models.DateTimeField(default=timezone.now)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title