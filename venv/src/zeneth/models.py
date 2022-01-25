from django.db import models

# Create your models here.

class villa(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='display_image_villa')
    desc = models.TextField()
    price = models.IntegerField()
    read_more_id = models.CharField(max_length=50)
    image_gallery_id = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class readMore(models.Model):
    
    img = models.ImageField(upload_to='readmore_image')
    read_more_id = models.CharField(max_length=50)
    def __str__(self):
        return self.read_more_id

class imageGallery(models.Model):
    
    img_1 = models.ImageField(upload_to='gallery_image')
    img_2 = models.ImageField(upload_to='gallery_image')
    img_3 = models.ImageField(upload_to='gallery_image')
    img_4 = models.ImageField(upload_to='gallery_image')
    img_5 = models.ImageField(upload_to='gallery_image')
    image_gallery_id = models.CharField(max_length=50)
    def __str__(self):
        return self.image_gallery_id



class privacyPolicy(models.Model):
    
    heading = models.CharField(max_length=100)
    desc = models.TextField()
    def __str__(self):
        return self.heading


class testimonial(models.Model):
    
    name = models.CharField(max_length=100)
    desc = models.TextField()
    def __str__(self):
        return self.name