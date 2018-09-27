from django.db import models

# Create your models here.

class Places(models.Model):
    location = models.CharField(max_length= 40)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length= 30)

    def __str__(self):
        return self.category

class Image(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    location = models.ForeignKey(Places)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return self.name

