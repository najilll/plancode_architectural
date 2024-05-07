from django.db import models

# Create your models here.
class Baner(models.Model):
    title = models.CharField(max_length=150)
    background_image = models.ImageField(upload_to="baner/")
    description=models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    background_image = models.ImageField(upload_to="portfolio/")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Transformation(models.Model):
    before = models.ImageField(upload_to="transformation/")
    after = models.ImageField(upload_to="transformation/")

    def __str__(self):
        return self.before.name

class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    image = models.ImageField(upload_to="employee/")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="baner/")
    description=models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name