from django.http import JsonResponse
from django.shortcuts import render
from backend.base.serializers import ProductSerializer
from rest_framework.decorators import api_view
from backend.base.models import Product
from rest_framework.response import Response
from base import products

# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/',
        '/api/products/',
        '/api/quizzes/',
    ]

    return Response(routes)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.filter(_id=pk).first()
    # need ung .first() to get first instance of object query set
    if product is None:
        return Response({'detail': 'Product not found'}, status=404)


    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)    