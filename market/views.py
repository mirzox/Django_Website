from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

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


class BrandView(APIView):
    def get(self, request):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetailView(APIView):
    def get_data(self, pk):
        try:
            data = Brand.objects.get(pk=pk)
            return data
        except ObjectDoesNotExist:
            raise Http404("Данные не найдены!!!")

    def get(self, request, pk):
        brand = self.get_data(pk=pk)
        serializer = BrandSerializer(brand)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        brand = self.get_data(pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"request": "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({"request": "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = self.get_data(pk=pk)
        try:
            brand.delete()
            data = {
                'request': 'Data successfully deleted'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {
                'request': 'Oops Something went wrong'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class NotebookView(APIView):
    def get(self, request):
        notebook = Notebook.objects.all()
        serializer = NotebookSerializer(notebook, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotebookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookDetailView(APIView):
    def get_data(self, pk):
        try:
            data = Notebook.objects.get(pk=pk)
            return data
        except ObjectDoesNotExist:
            raise Http404("Данные не найдены!!!")

    def get(self, request, pk):
        notebook = self.get_data(pk=pk)
        serializer = NotebookSerializer(notebook)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        notebook = self.get_data(pk=pk)
        serializer = NotebookSerializer(notebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"request": "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({"request": "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notebook = self.get_data(pk=pk)
        try:
            notebook.delete()
            data = {
                'request': 'Data successfully deleted'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {
                'request': 'Oops Something went wrong'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class NotebookApiView(APIView):
    def get(self, request):
        notebook_detail = NotebookDetail.objects.all()
        serializer = NotebookSerializer(notebook_detail, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotebookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookDetailApiView(APIView):
    def get_data(self, pk):
        try:
            data = NotebookDetail.objects.get(pk=pk)
            return data
        except ObjectDoesNotExist:
            raise Http404("Данные не найдены!!!")

    def get(self, request, pk):
        notebook_detail = self.get_data(pk=pk)
        serializer = NotebookDetailSerializer(notebook_detail)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        notebook_detail = self.get_data(pk=pk)
        serializer = NotebookDetailSerializer(notebook_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"request": "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({"request": "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notebook_detail = self.get_data(pk=pk)
        try:
            notebook_detail.delete()
            data = {
                'request': 'Data successfully deleted'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {
                'request': 'Oops Something went wrong'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
