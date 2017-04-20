from rest_framework import serializers
from django.contrib.auth.models import User
from pub_keys.models import PublicKey

class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicKey
        fields = ('id', 'created', 'last_updated', 'key_owner', 'pub_key', 'fingerprint', 'is_validated')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
