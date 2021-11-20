from django.contrib import admin

# Register your models here.

from core.models import RecursoImagem, RecursoVideo

admin.site.register(RecursoImagem)
admin.site.register(RecursoVideo)