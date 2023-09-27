import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST
)


# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # check if username and password not not
    if username is None and password is None:
        return Response(status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response(HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    user_detail = User.objects.get(pk=user.pk)

    return Response({
        'token': token.key,
        'user_id': user.pk,
        'email': user_detail.email,
        'username': user_detail.username,
        'is_active': user_detail.is_active,
        'is_admin': user_detail.is_superuser,
        'join_date': user_detail.date_joined
    }, status=HTTP_200_OK)
