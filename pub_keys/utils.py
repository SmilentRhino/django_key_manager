import base64
import binascii
import paramiko
import string
from random import sample, choice

def get_fingerprint(public_key):
    """
    """
    try:
        pub_key = public_key.split()
        mykey = paramiko.rsakey.RSAKey(data=base64.b64decode(pub_key[1].strip()))
    except Exception as e:
        return ''
    fingerprint = binascii.hexlify(mykey.get_fingerprint()).decode()
    return fingerprint

def generate_password():
    chars = string.letters + string.digits
    length = 16
    return ''.join([choice(chars) for i in range(length)])


def validate_password():
    return
