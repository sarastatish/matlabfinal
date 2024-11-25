
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

import myapp

urlpatterns = [

    path('', include('myapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
