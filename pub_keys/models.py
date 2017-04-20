from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_pubkey(value):
    if value:
        pass

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
    
