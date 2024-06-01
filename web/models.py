from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class Baner(models.Model):
    title = models.CharField(max_length=150)
    background_image = models.ImageField(upload_to="baner/")
    description=models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class PortfolioCategory(models.Model):
    title = models.CharField(max_length=150,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=150)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    descriptions = HTMLField()
    background_image = models.ImageField(upload_to="portfolio/")
    is_home = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("web:portfolio-details", kwargs={"slug": self.slug})
    
    
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
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    image = models.ImageField(upload_to='blog/image/', blank=True, null=True)
    description = HTMLField()
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("web:blog-details", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('date',)
        verbose_name = ('News & Update')
        verbose_name_plural = ("News & Updates")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    message=models.TextField()
    
    def __str__(self):
        return self.name