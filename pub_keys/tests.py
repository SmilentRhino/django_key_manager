from django.test import TestCase
from django.contrib.auth.models import User
from pub_keys.models import PublicKey

# Create your tests here.

class PublicKeyTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='alexrhino', password='password')
        PublicKey.objects.create(key_owner=user, 
            pub_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCsekgDsepUXl228ClYa4B8IX8lTs40wgRT2YYKx08wDDE+E9yUOrKMQpH0UdIr5xdJJFhRm9Bcgq4YU37r13OeKdR4wXx4nYtJ2Tk7G9jHAA2h3LPapPpHvNrlrn7P1n8eRcahjGKqHTIp9RDrHzsg7ZX7U8wjZB6ovCYd736DfVHwgWP9wHTXna9cldmPJh4mmbPXiwyQrKSRj7bzT9V5EUp1LvJtM9FoaAiQcDatzYGNOQEARwPxosxjc2ZEQR+6K2ekjHLT893y+9LDewTqaQhXuzBiU5md8sVulIBNElXLHsAvx9uX7b1u/it/i7Rmc8A8GTerII7rH87rnVEa+UJEIdfWY6qReKUBcvnBmjTms76r+nNZ9/Dc2G1sHvOefIR1e9YPUCs1zhNpuzGwcpDpN6EQW9sAuqmdmpl9Bz4yW1uHJDLQPr/ABUinP89sEiVEYLxocD1u4JqsYae/P6iFxgcGZsp7b5RgAJ2nMkUN306FLof1frGCwMZWI4Kaj1/+vI5fPMVPLyFqXvvB/nEHajWXWOdI22PTCj4VaJ4/ch6lkbDYfRQB83nJW8W1/rDyhqJ8e3wXJLf9zhnrKJp2WCFIeMmCxu0eZMJ+yUoKwUcPdVyK5Jj4BXhvUOH9aUPPCBf/lkwyVJhfppvztmWoWEJxPF3bjVoCMXyw/w== ubuntu@workandstudy.a.r', fingerprint='39ce959c40f4add85b5162e137b742c5')
        
    def test_fetch_pubkey(self):
        pubkey = PublicKey.objects.get(key_owner__username='alexrhino')
        self.assertEqual(pubkey.fingerprint ,'39ce959c40f4add85b5162e137b742c5')
