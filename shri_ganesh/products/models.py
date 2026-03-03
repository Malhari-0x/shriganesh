from django.db import models


class Product(models.Model):
    BRAND_CHOICES = [
        ('Asian Paints', 'Asian Paints'),
        ('Birla Opus', 'Birla Opus'),
        ('Surfa Coat', 'Surfa Coat Paints'),
        ('Rajyog', 'Rajyog Paints'),
    ]

    CATEGORY_CHOICES = [
        ('Interior', 'Interior'),
        ('Exterior', 'Exterior'),
        ('Primer', 'Primer'),
        ('Waterproofing', 'Waterproofing'),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
