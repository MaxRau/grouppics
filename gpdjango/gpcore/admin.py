from django.contrib import admin
from gpcore.models import gpUser
from gpcore.models import gpAlbum
from gpcore.models import gpPhoto
# Register your models here.
admin.site.register(gpUser)
admin.site.register(gpAlbum)
admin.site.register(gpPhoto)
