from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import migrations, models
from django.utils.timezone import utc



# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    post = HTMLField()
    caption = models.TextField(max_length=50)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=60)
    profile_image = models.ImageField(upload_to='profiles/',blank=True)
    pub_date = models.DateTimeField(default=1)



    def __str__(self):
        return self.caption

    def save_images(self):
        self.save()

    def delete_images():
        self.delete()


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

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save

    def delete_profile(self):
        self.delete()

class StazoneLetterRecipients(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField()


class comment(models.Model):
    text =models.CharField(max_length=100,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)

class Follow(models.Model):
    # follower = models.OneToMany(User)
    current_user = models.ForeignKey(User,null=True)
