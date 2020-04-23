from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sites.models import Site
from .utils import send_notification
from ckeditor.fields import RichTextField
import os

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.title, ext)
    return os.path.join('uploads', filename)

class ResourceMixin(models.Model):
    title  = models.CharField(max_length=100)
    desc  = models.TextField(null=True, blank=True)
    date  = models.DateTimeField(default=timezone.now)
    image  = models.ImageField(upload_to="uploads/images", blank=True, null=True)
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 
    file  = models.FileField(upload_to=content_file_name)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_readable_date(self):
        return self.date.strftime("%a, %B %d. %I:%M %p")
        
    def get_file_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.file.url
        return f"{domain}{path}"
    
    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.image.url
        return f"{domain}{path}"

class Photo(ResourceMixin):
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        send_notification("New Photo", 
                f"New Photo has been added, open 'Photos' to listen; 'Title: {self.title}'")
                
class Audio(ResourceMixin):
    def save(self, *args, **kwargs):
        super(Audio, self).save(*args, **kwargs)
        send_notification("New Audio", 
                f"New audio has been added, open 'Audios' to listen; 'Title: {self.title}'")

class Video(ResourceMixin):
    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)
        send_notification("New Video", 
                f"New video has been added, open 'Videos' to listen; 'Title: {self.title}'")

class Material(ResourceMixin):
    def save(self, *args, **kwargs):
        super(Material, self).save(*args, **kwargs)
        send_notification("New Material", 
                f"New book has been added, open 'Library' to view; 'Title: {self.title}'")

    def update(self, *args, **kwargs):
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
    church_id      = models.CharField(max_length=15, default="1")
    momo           = models.CharField(max_length=15, null=True, blank=True)
    contact        = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class DailyDevotion(models.Model):
    title       = models.CharField(max_length=100)
    content     = RichTextField(null=True, blank=True)
    date        = models.DateTimeField(default=timezone.now)
    background  = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    church      = models.ForeignKey("Church", on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        super(DailyDevotion, self).save(*args, **kwargs)
        send_notification("Daily Devotion", 
                self.content)

    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.image.url
        return f"{domain}{path}"
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Notification(models.Model):
    title   = models.CharField(max_length=100)
    message = models.TextField()
    date    = models.DateTimeField(default=timezone.now)
    church = models.ForeignKey("Church", on_delete=models.CASCADE) 

    def get_readable_date(self):
        return self.date.strftime("%a, %B %d. %I:%M %p")

    def save(self, *args, **kwargs):
        super(Notification, self).save(*args, **kwargs)
        send_notification(self.title, self.message)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
    
class Testimony(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonies")
    testimony = models.TextField()
    date      = models.DateTimeField(default=timezone.now)
    viewed      = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class PrayerRequest(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prayer_requests")
    request = models.TextField()
    date        = models.DateTimeField(default=timezone.now)
    viewed      = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user  = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="feedbacks")
    feedback = models.TextField()
    date        = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.feedback