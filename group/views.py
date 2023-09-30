from datetime import datetime
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from group.models import Group
from group.serializer import GroupSerializer
from app.globalVariable import ResponseMessage

# Create your views here.

# global variable
model = Group


class GroupView(APIView):
    """ group views private variable

    List all group, or create a new group.
    """

    def get(self, request, format=None):
        try:
            # import pdb
            # pdb.set_trace()
            data = Group.objects.all()
            serializer = GroupSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as exe:
            Exception(exe)
            return Response(data=ResponseMessage.error_message, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        try:
            if request.method == 'POST':
                serializer = GroupSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(created_by=request.user,
                                    created_at=datetime.now())
                    return Response({'msg': 'data successfully added'}, status=status.HTTP_201_CREATED)
        except Exception as exe:
            Exception(exe)
            return Response(data=ResponseMessage.error_message, status=status.HTTP_400_BAD_REQUEST)


class GroupDetail(APIView):
    """_GroupDetail

     Retrieve, update or delete a group instance.
    """

    def get(self, request, pk, format=None):
        try:
            if request.method == 'GET':
                group = model.objects.get(pk=pk)
                serializer = GroupSerializer(group)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except model.DoesNotExist as exe:
            logging.error(exe)
            return Response(ResponseMessage.error_message, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            if request.method == 'PUT':
                group = model.objects.get(pk=pk)
                serializer = GroupSerializer(group, request.data)
                if serializer.is_valid():
                    serializer.save(updated_at=datetime.now(),
                                    updated_by=request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Group.DoesNotExist as exe:
            logging.error(exe)
            return Response(data=ResponseMessage.error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            msg = {'message': 'data Delete.'}
            Group.objects.get(pk=pk).delete()
            return Response(msg, status=status.HTTP_200_OK)
        except model.DoesNotExist as exe:
            logging.error(exe)
            return Response(data=ResponseMessage.error_message, status=status.HTTP_400_BAD_REQUEST)
