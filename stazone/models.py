from django.db import models

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

class Profile(models.Model):
    bio =models.TextField(max_length=60)
    profile_pic = models.ImageField(upload_to='profile/')
