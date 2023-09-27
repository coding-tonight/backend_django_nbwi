import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from group.models import Group
from group.serializer import GroupSerializer

# Create your views here.
class GroupView(APIView):
    """ group views private variable

    List all group, or create a new group.
    """
    model = Group

    try:
        data = model.objects.raw("select * from salegroup")
    except:
        logging.error('group model does not exist')

    def get(self, request, format=None):
        if request.method == 'GET':
            serializer = GroupSerializer(self.data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = GroupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupDetail(APIView):
    """_GroupDetail

     Retrieve, update or delete a group instance.
    """
    model = Group

    def get_objects(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist as exe:
            logging.error(exe)
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_objects(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        group = self.get_objects(pk)
        serializer = GroupSerializer(group, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_objects(pk)
        group.delete()
        return Response(status=status.HTTP_200_OK)
