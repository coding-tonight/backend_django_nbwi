import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.response import Response
from item.serializer import ItemSerializer
from item.models import Item

# Create your views here.

# global variable
model = Item


class ItemView(APIView):
    """item views

      view to get all list of the item and add item
    """
    try:
        products = model.objects.raw('select * from item')
    except model.DoesNotExist as exe:
        logging.error(exe)

    def get(self, request, format=None):
        if request.method == 'GET':
            serializer = ItemSerializer(self.products, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    """item view for detail

     to get , update , delete item
    """

    def get_objects(self, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist as exe:
            logging.error(exe)
            return Http404

    def get(self, request, pk, format=None):
        if request.method == 'GET':
            product = self.get_objects(pk)
            serializer = ItemSerializer(product)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        if request.method == 'PUT':
            product = self.get_objects(pk)
            serializer = ItemSerializer(product, data=request.data)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if request.method == 'DELETE':
            product = self.get_objects(pk)
            product.delete()
            return Response({"message": "item has been deleted successfully"})
        return Response(status=HTTP_400_BAD_REQUEST)
