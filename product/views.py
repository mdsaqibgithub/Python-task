from django.shortcuts import get_object_or_404, render
from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return Response({'message': "Product deleted successfully!"},status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': "Product not found"}, status=status.HTTP_404_NOT_FOUND)
