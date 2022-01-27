from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist,
from django.shortcuts import get_object_or_404

from .models import Category, Brand, NotebookDetail, Notebook
from .serializers import CategorySerializer, BrandSerializer, NotebookDetailSerializer, NotebookSerializer


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_data(self, pk):
        try:
            data = Category.objects.get(pk=pk)
            return data
        except ObjectDoesNotExist:
            raise Http404("Данные не найдены!!!")

    def get(self, request, pk):
        category = self.get_data(pk=pk)
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.get_data(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"request": "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({"request": "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_data(pk=pk)
        try:
            category.delete()
            data = {
                'request': 'Data successfully deleted'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {
                'request': 'Oops Something went wrong'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
