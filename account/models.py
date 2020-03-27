from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    full_name   = models.CharField(max_length=100)
    image       = models.ImageField(upload_to="uploads/users")

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

