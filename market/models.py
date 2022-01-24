from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    items_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class NotebookDetail(models.Model):
    cpu = models.CharField(max_length=50)
    ram = models.IntegerField()
    gpu = models.CharField(max_length=100)
    ssd = models.CharField(max_length=50, null=True, blank=True)
    hdd = models.CharField(max_length=50, null=True, blank=True)
    os = models.CharField(max_length=30)
    display_size = models.CharField(max_length=50)
    display_type = models.CharField(max_length=50)
    year_of_issue = models.DateField()

    class Meta:
        verbose_name = 'NotebookDetail'
        verbose_name_plural = 'NotebookDetails'


class Notebook(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    detail = models.ForeignKey(NotebookDetail, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'


@receiver(post_save, sender=Notebook)
def check_status(sender, instance, created, **kwargs):
    if created:
        category = Category.objects.get(pk=instance.category)
        category.items_count += 1
        category.save()


