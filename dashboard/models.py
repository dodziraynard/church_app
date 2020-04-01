from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sites.models import Site


class ResourceMixin(models.Model):
    title  = models.CharField(max_length=100)
    desc  = models.TextField(null=True, blank=True)
    date  = models.DateTimeField(default=timezone.now)
    image  = models.ImageField(upload_to="uploads/images")
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 

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

    def save(self, *args, **kwargs):
        self.file.name = self.title+"."+self.file.name.split(".")[-1]
        super(Material, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        self.file.name = self.title+"."+self.file.name.split(".")[-1]
        super(Material, self).update(*args, **kwargs)
    
class Leader(models.Model):
    position    = models.CharField(max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE) 
    contacts    = models.CharField(max_length=50)
    date        = models.DateTimeField(default=timezone.now)
    inactive    = models.DateTimeField(null=True, blank=True)
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 

    def get_full_name(self):
        return self.user.profile.full_name

    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.user.profile.image.url
        return f"{domain}{path}"

    def __str__(self):
        return self.position

    def __unicode__(self):
        return self.position

class Church(models.Model):
    name           = models.CharField(max_length=100)
    about          = models.TextField()
    address        = models.TextField()
    head_pastor    = models.CharField(max_length=100) 
    help_text      = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class DailyDevotion(models.Model):
    image       = models.ImageField(upload_to="uploads/Devotions")
    content = models.TextField() 
    verse       = models.CharField(max_length=100)
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 

    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.image.url
        return f"{domain}{path}"
    def __str__(self):
        return self.verse

    def __unicode__(self):
        return self.verse

class Notification(models.Model):
    title   = models.CharField(max_length=100)
    message = models.TextField()
    date    = models.DateTimeField(default=timezone.now)
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title