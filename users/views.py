import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.models import UserConfirm
from users.serializers import RegisterSerializer, LoginUserSerializer, UserConfirmSerializer


# Create your views here.


@api_view(['POST'])
def user_register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    confirmation = UserConfirm.objects.create(user=user, code=random.randint(1000, 9999))
    return Response({'status': "User register", 'code': confirmation.code, 'data': serializer.data},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_user(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')
    confirm = get_object_or_404(UserConfirm, code=code)
    user = confirm.user
    user.is_active = True
    user.save()
    confirm.delete()
    return Response({'m': 'User Active !!'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def login_user(request):
    serializer = LoginUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    login(request, user)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        user.save()
        return Response({'token': token.key})
    return Response({'error': 'неправильно'}, status=400)
