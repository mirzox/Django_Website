from django.db import models
from django.db.models.signals import post_save, pre_delete
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    items_count = models.IntegerField(default=0)
    total_cost = models.FloatField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    about = models.TextField()
