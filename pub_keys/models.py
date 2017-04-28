import subprocess
import paramiko
import base64
import binascii
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from pub_keys.validators import validate_pubkey

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class PublicKey(models.Model):
    '''
    A 10240 bits created by sshkeygen is around 1800 characters, so I ssh_key here is reasonable to have a maxlength of 5000
    '''
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    key_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    pub_key = models.CharField(max_length=5000, validators=[validate_pubkey])
    fingerprint = models.CharField(max_length=200, unique=True)
    is_validated = models.BooleanField(default=False)
    
    def clean(self):
        try:
           pub_key = self.pub_key.split()
           mykey = paramiko.rsakey.RSAKey(data=base64.b64decode(pub_key[1].strip()))
        except Exception as e:
            raise ValidationError(
                _(str(e)),
             )
        self.fingerprint = binascii.hexlify(mykey.get_fingerprint()).decode()
    
    def __str__(self):
        return self.fingerprint
