from django.urls import path
from .views import  get_photos , search_photos

urlpatterns = [
    path('', get_photos, name='getphoto'),
    path('search/', search_photos, name='search'),
    #path('', index_view, name='index'),
]