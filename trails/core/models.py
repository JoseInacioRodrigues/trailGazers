from django.db import models

# Create your models here.

class Resource(models.Model):
    pass


class VideoResource(models.Model):
    created_at = models.DateField(auto_now_add=True)
    video = models.FileField(upload_to='videos', default=None)
    content = models.TextField(default='')
    enable = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'videos'  
        verbose_name_plural = "VideoResources" 

    def __str__(self):
        return self.content 


class ImageResource(models.Model):
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images',default=None)
    content = models.TextField(default='')
    enable = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'images' 
        verbose_name_plural = "ImageResources"

    def __str__(self):
        return self.content 
