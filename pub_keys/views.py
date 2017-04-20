from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from pub_keys.serializers import PublicKeySerializer, UserSerializer
from pub_keys.models import PublicKey

class PublicKeyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = PublicKey.objects.all()
    serializer_class = PublicKeySerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
