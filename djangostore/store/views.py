# Create your views here.
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import Category, Product
from .serializers import CategorySerializer, Product


@api_view(['GET'])
def categoryOverView(request):
    # check if user is admin
    # permission_classes = (IsAdmin,)

    api_urls = {
        "all_categorys": '',
        'Add': 'create',
        'Update': 'pk/update',
        'Delete': 'pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_categorys(request):
    # check if user is admin
    # permission_classes = (IsAdmin,)

    category = CategorySerializer(data=request.data)

    # validating for already existing data
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if category.is_valid():
        category.save()
        return Response(category.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_categorys(request):

    if request.query_params:
        categorys = Category.objects.get(**request.query_param.dict())
    else:
        categorys = Category.objects.all()
    
    if categorys:
        data = CategorySerializer(categorys, many=True)
        return Response(data.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def detail_category(request,pk):

    categorys = Category.objects.get(pk=pk)
    
    if categorys:
        data = CategorySerializer(categorys, many=False)
        return Response(data.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    data = CategorySerializer(instance=category, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    if category != None:
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def product_list(request):
    # check if user is admin
    # permission_classes = (IsAdmin,)

    if request.query_params:
        products = Product.objects.get(**request.query_param.dict())
    else:
        products = Product.objects.all()
    
    if products:
        data = ProductSerializer(products, many=True)
        return Response(data.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_products(request):
    # check if user is admin
    # permission_classes = (IsAdmin,)

    product = ProductSerializer(data=request.data)

    # validating for already existing data
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if product.is_valid():
        product.save()
        return Response(category.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    