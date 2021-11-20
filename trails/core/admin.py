from django.contrib import admin

# Register your models here.

from core.models import ImageResource, VideoResource

admin.site.register(ImageResource)
admin.site.register(VideoResource)