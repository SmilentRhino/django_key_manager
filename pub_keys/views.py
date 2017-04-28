import random
import django_filters
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from pub_keys.serializers import PublicKeySerializer, UserSerializer
from pub_keys.models import PublicKey
from pub_keys.validators import validate_pubkey
from pub_keys.utils import generate_password, get_fingerprint

class PublicKeyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    authentication_classes = (SessionAuthentication,TokenAuthentication )
    permission_classes = (IsAuthenticated,)
    queryset = PublicKey.objects.all()
    serializer_class = PublicKeySerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    authentication_classes = (SessionAuthentication,TokenAuthentication ,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['post'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAdminUser,))
@renderer_classes((StaticHTMLRenderer,))
def add_key(request):
    email =  request.data.get('email')
    username =  request.data.get('username')
    password =  request.data.get('password')
    pubkey =  request.data.get('pubkey')
    if not email:
        return Response('User email should be provided!')
    if not pubkey:
        return Response('Publike key should be provided!')
    try:
        validate_email(email)
        validate_pubkey(pubkey)
        if not username:
            username = email.split('@')[0]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            if not password:
                password = str(random.random())
            user = User.objects.create_user(username, email, password)

        fingerprint = get_fingerprint(pubkey)
        try:
            public_key = PublicKey.objects.get(fingerprint = fingerprint) 
            return Response('The key already exsits')
        except PublicKey.DoesNotExist:
            public_key = PublicKey.objects.create(key_owner=user, pub_key = pubkey, fingerprint=fingerprint)
    except Exception as e:
        return Response(str(e))
    return Response('New key added!')

    
