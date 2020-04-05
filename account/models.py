from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Church
from django.contrib.sites.models import Site
from django.utils import timezone

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    full_name   = models.CharField(max_length=100)
    mobile      = models.CharField(max_length=15)
    image       = models.ImageField(upload_to="uploads/users", default="assets/avatar.png")
    church      = models.ForeignKey(Church, default=1, on_delete=models.CASCADE, related_name='profiles')
    date       = models.DateTimeField(default=timezone.now)
    
    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_church(self):
        return self.church.name

    def get_image_url(self):
        domain = Site.objects.get(name="production").domain
        path = self.image.url
        return f"{domain}{path}"

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

