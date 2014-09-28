from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class gpAlbum(models.Model):
    # TODO Add contributor users
    # TODO Add viewer users
    
    album_date_created = models.DateTimeField(auto_now_add=True)
    album_title = models.CharField(max_length=30)
    album_public = models.BooleanField(default=False)

    def __unicode__(self):  
        return self.album_title

class gpPhoto(models.Model):

    photo_title = models.CharField(max_length=30, null=True)
    photo_album = models.ForeignKey(gpAlbum, null=True, blank=True)
    photo_uploader = models.ForeignKey(User, null=True, blank=True)
    photo_date_created = models.DateTimeField(auto_now_add=True)
    photo_image = models.FileField(upload_to="photos/")
	# TODO Add Imagefield

    def __unicode__(self):  
        return self.photo_title

class gpAdminAlbum(admin.ModelAdmin):
    search_fields = ["album_title"]
    list_display = ["album_title"]

class gpAdminPhoto(admin.ModelAdmin):
    search_fields = ["photo_title"]
    list_display = ["__unicode__", "photo_title", "photo_album", "photo_uploader", "photo_date_created"]

