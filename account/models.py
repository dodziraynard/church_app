from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Church

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    full_name   = models.CharField(max_length=100)
    mobile      = models.CharField(max_length=15)
    image       = models.ImageField(upload_to="uploads/users")
    church      = models.ForeignKey(Church, default=1, on_delete=models.CASCADE, related_name='profiles')

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

