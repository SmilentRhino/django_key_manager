import base64
import paramiko
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_pubkey(value): 
    if value: 
        pub_key = value.split() 
        if pub_key[0] == 'ssh-rsa': 
            try: 
               mykey = paramiko.rsakey.RSAKey(data=base64.b64decode(pub_key[1])) 
            except Exception as e: 
                raise ValidationError( 
                    _(str(e)), 
             ) 
            if mykey.size < 4096: 
                raise ValidationError( 
                    _('This key is not strong enough, at least 4096 required'), 
             ) 
                  
        else: 
            raise ValidationError( 
                _('Unsupported Key Type'), 
        ) 
    return True 
