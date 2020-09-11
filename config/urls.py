
from django.contrib import admin
from django.urls import path

BASE_URL = 'https://api.unsplash.com/'

urlpatterns = [
    path('admin/', admin.site.urls),
]
