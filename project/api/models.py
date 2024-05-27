from django.db import models


# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='hero/')
    image_name = models.CharField(max_length=100)
    image_size = models.CharField(max_length=100)
    image_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    image_name = models.CharField(max_length=100)
    image_size = models.CharField(max_length=100)
    image_type = models.CharField(max_length=100)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')
    image_name = models.CharField(max_length=100)
    image_size = models.CharField(max_length=100)
    image_type = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.ManyToManyField("Skill")
    image = models.ImageField(upload_to='projects/')
    image_name = models.CharField(max_length=100)
    image_size = models.CharField(max_length=100)
    image_type = models.CharField(max_length=100)
    link = models.URLField(max_length=250)
    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    content = models.TextField()
    def __str__(self):
        return self.name

