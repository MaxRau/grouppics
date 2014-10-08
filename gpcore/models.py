from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
import string
import os
from PIL import Image as PILImage

# Create your models here.

class gpAlbum(models.Model):
    # TODO Add contributor users
    # TODO Add viewer users
    
    album_date_created = models.DateTimeField(auto_now_add=True)
    album_title = models.CharField(max_length=30)
    album_public = models.BooleanField(default=False)
    
    def images(self):
	lst = [x.image.name for x in self.image_set.all()]
	lst = ["<a href='/assets/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')

    def __unicode__(self):  
        return self.album_title

class gpPhoto(models.Model):

    photo_title = models.CharField(max_length=30, null=True)
    photo_album = models.ForeignKey(gpAlbum, null=True, blank=True)
    photo_uploader = models.ForeignKey(User, null=True, blank=True)
    photo_date_created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="photos/")

    photo_width = models.IntegerField(null = True, blank = True)
    photo_height = models.IntegerField(null = True, blank = True)
    
    def saveDimensions(self, *arg, **kwargs):
        super(gpPhoto, self).save(*args, **kwargs)
	image = PILImage.open(os.path.join(MEDIA_ROOT, self.image.name))
	self.photo_width, self.photo_height = image.size
	super(Image, self).save(*args, **kwargs)

    def size(self):
        return "%s x %s" % (self.photo_width, self.photo_height)

    def thumbnail(self):
        return """<img border="0" alt="" src="/assets/%s" height="40" />""" % ((self.image.name))

    def __unicode__(self):  
        return self.photo_title

class gpAdminAlbum(admin.ModelAdmin):
    search_fields = ["album_title"]
    list_display = ["album_title"]

class gpAdminPhoto(admin.ModelAdmin):
    #search_fields = ["photo_title"]
    list_display = ["__unicode__", "photo_title", "photo_album", "photo_uploader", "size", "thumbnail", "photo_date_created"]
    list_filter = ["photo_uploader"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
	obj.save()

