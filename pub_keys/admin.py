from django.contrib import admin
from pub_keys.models import PublicKey
from pub_keys.forms import PublicKeyForm
# Register your models here.


class PublicKeyAdmin(admin.ModelAdmin):
    form = PublicKeyForm
    readonly_fields = ('fingerprint',)

admin.site.register(PublicKey, PublicKeyAdmin)
