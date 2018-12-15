from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    post = HTMLField()
    caption = models.TextField(max_length=50)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField()
    comments = models.CharField(max_length=60)
    profile_image = models.ImageField(upload_to='profiles/',blank=True)
