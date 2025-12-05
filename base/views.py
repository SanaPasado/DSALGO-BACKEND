from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
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
    return Response(products)

@api_view(['GET'])
def get_product(request, pk):
    product = None
    for item in products:
        if item['_id'] == pk:
            product = item
            break

    return Response(product)    