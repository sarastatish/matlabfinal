
from django.contrib import admin
from django.urls import path,include

import myapp

urlpatterns = [

    path('', include('myapp.urls')),

]
