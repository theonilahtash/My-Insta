from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    # post = HTMLField()
    caption = models.TextField(max_length=50)
    # profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField()
    comments = models.CharField(max_length=60)
    profile_image = models.ImageField(upload_to='profiles/',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.caption


    @classmethod
    def stazone_today(cls):
        stazone = cls.objects.filter(pub_date__date = today)
        return stazone

    @classmethod
    def search_profile(cls,search_term):
        profile = cls.objects.filter(username_icontains=query)
        return profile


class Profile(models.Model):
    bio =models.TextField(max_length=60)
    profile_pic = models.ImageField(upload_to='profile/')
