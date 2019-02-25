from django.db import models
from django.contrib.auth import models
# Create your models here.
"""
class CustomUser(User, PermissionsMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)
    joined_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return "@{}".format(self.username)
"""
class User(models.User, models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)