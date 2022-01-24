# Generated by Django 4.0 on 2022-01-24 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('items_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='NotebookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('gpu', models.CharField(max_length=100)),
                ('ssd', models.CharField(blank=True, max_length=50, null=True)),
                ('hdd', models.CharField(blank=True, max_length=50, null=True)),
                ('os', models.CharField(max_length=30)),
                ('display_size', models.CharField(max_length=50)),
                ('display_type', models.CharField(max_length=50)),
                ('year_of_issue', models.DateField()),
            ],
            options={
                'verbose_name': 'NotebookDetail',
                'verbose_name_plural': 'NotebookDetails',
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.category')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.notebookdetail')),
            ],
            options={
                'verbose_name': 'Notebook',
                'verbose_name_plural': 'Notebooks',
            },
        ),
    ]