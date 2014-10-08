from django.contrib import admin
from gpcore.models import gpAlbum
from gpcore.models import gpPhoto
from gpcore.models import gpAdminAlbum
from gpcore.models import gpAdminPhoto
# Register your models here.
admin.site.register(gpAlbum, gpAdminAlbum)
admin.site.register(gpPhoto, gpAdminPhoto)
