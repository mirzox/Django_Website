from rest_framework import serializers

from .models import Category, Brand, NotebookDetail, Notebook


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class NotebookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotebookDetail
        fields = "__all__"


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = "__all__"
