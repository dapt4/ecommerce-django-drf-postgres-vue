from .models import Product, Order, OrderItem
from .serializer import ProductSerializer, OrderItemSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import traceback
import json

# Create your views here.


@api_view(['GET', 'POST'])
def get_all_create(request):
    try:
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
    except Exception:
        traceback.print_exc()
        return Response({'error': '500'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def get_one_edit_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            product.delete()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception:
        traceback.print_exc()
        return Response({'error': '500'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def order(request):
    try:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #order = Order.objects.get(id=serializer.data['id'])
            #order_items = order.items.all()
            #serializer2 = OrderItemSerializer(order_items, many=True)
            '''
            ahora a devolver la lista de items y el monto a pagar, para ello
            crear un modelo de invoice (factura) y un serializer
            '''
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"error": 'the data is not valid'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception:
        traceback.print_exc()
        return Response({'error': '500'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
