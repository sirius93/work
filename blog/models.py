from __future__ import unicode_literals
import datetime
import markdown
from django_markdown.models import MarkdownField

from django.db import models

from django.conf import settings

from django.utils import timezone

def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="blog/static/upload/images" )

    def __unicode__( self ):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1000,default='')
    text = models.TextField()
    images = models.ManyToManyField( Image, blank=True )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def body_html( self ):
        return markdown_to_html( self.body, self.images.all() )
# Create your models here.