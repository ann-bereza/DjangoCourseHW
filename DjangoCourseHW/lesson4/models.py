from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, default='slug')

    class Meta:
        app_label = 'lesson4'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, default='slug')

    class Meta:
        app_label = 'lesson4'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'lesson4'

    def __str__(self):
        return self.name
