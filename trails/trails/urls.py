"""trails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path, re_path
from django.conf.urls.static import static
from django.conf import settings
from core.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("core.api.urls")),

    path("api-auth/", include("rest_framework.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #re_path("", IndexTemplateView.as_view(), name="entry-point")
    re_path(r"^app/*$", IndexTemplateView.as_view(), name="entry-point"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += re_path("", IndexTemplateView.as_view(), name="entry-point")
