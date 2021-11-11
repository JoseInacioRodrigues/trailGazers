from django.contrib import admin
from api.models import (
    AppTranslations, Author,
    AuthorThecnicalInformation,
    Countries, Culture,CultureTechnicalInformation,
    Dictionary, Facts, FactsTechnicalInformation,
    Idioma, Languages, Logs, Plants
)
admin.site.register(AppTranslations)
admin.site.register(Author)
admin.site.register(AuthorThecnicalInformation)
admin.site.register(Countries)
admin.site.register(Culture)
admin.site.register(CultureTechnicalInformation)
admin.site.register(Dictionary)
admin.site.register(Facts)
admin.site.register(FactsTechnicalInformation)
admin.site.register(Idioma)
admin.site.register(Languages)
admin.site.register(Logs)
admin.site.register(Plants)

