from django.db import models

# Create your models here.

class gpUser(models.Model)
    user_name = models.CharField(max_length=25)
    user_password = models.CharField(max_length=25)
    user_date_joined = models.DateTimeField('date joined')

class gpAlbum
    creator = models.ForeignKey(gpUser)
    # TODO Add contributor users
    # TODO Add viewer users
    
    album_date_created = models.DateTimeField('date created')
    album_title = models.CharField(max_length=25)
    album_public = models.BooleanField(initial=True)

class gpPhoto

    album = models.ForeignKey(gpAlbum)
    uploader = models.ForeignKey(gpUser)

    title = models.CharField(Max_length=25)
    # TODO Add Imagefield
