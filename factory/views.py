import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from factory.serializer import FactoryOwnerSerializer, FactorySerializer
from factory.models import Factory, FactoryOwner

# Create your views here.


class FactoryView(APIView):
    """Factory view to list all  data and add

    """
    model = Factory

    try:
        factory = model.objects.raw('select * from factory')

    except model.DoesNotExist as exe:
        logging.error(exe)

    def get(self, request, format=None):
        if request.method == 'GET':
            serializer = FactorySerializer(self.factory, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.method == 'POST':
            # print(request.data)
            serializer = FactorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)


class FactoryDetail(APIView):
    """FactoryDetail class to reterive data with id or pk , update  and delete

    """
    model = Factory

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist as exe:
            logging.error(exe)
            return Http404

    def get(self, request, pk, format=None):
        if request.method == 'GET':
            factory = self.get_object(pk)
            serializer = FactorySerializer(factory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        if request.method == 'PUT':
            factory = self.get_object(pk)
            serializer = FactorySerializer(factory, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        factory = self.get_object(pk)
        factory.delete()
        return Response({"message": "factory deleted successfully"}, status=status.HTTP_200_OK)


"""factory owner view
"""


class FactoryOwnerView(APIView):
    model = FactoryOwner

    try:
        factory_owner = model.objects.raw('select * from factoryowner')
    except model.DoesNotExist as exe:
        logging.error(exe)

    def get(self, request, format=None):
        if request.method == 'GET':
            serializer = FactoryOwnerSerializer(
                self.factory_owner, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = FactoryOwnerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FactoryOwnerDetail(APIView):
    """ factory detail to get , update , delete the factory owner data

    """
    model = FactoryOwner

    def get_objects(self, pk):
        try:
            return self.model.objects.get(pk=pk)

        except self.model.DoesNotExist as exe:
            logging.error(exe)
            return Http404

    def get(self, request, pk, format=None):
        if request.method == 'GET':
            factory_owner = self.get_objects(pk)
            serializer = FactoryOwnerSerializer(factory_owner)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        if request.method == 'PUT':
            factory_owner = self.get_objects(pk)
            serializer = FactoryOwnerSerializer(
                factory_owner, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if request.method == 'DELETE':
            factory_owner = self.get_objects(pk)
            factory_owner.delete()
            return Response({"message": "successfully deleted"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
