from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Post
from .models import Image

admin.site.register(Post)

admin.site.register(Image)



# Register your models here.