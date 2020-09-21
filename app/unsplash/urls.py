from django.urls import path
from .views import  index_view , search_photos , detail_view , get_photos

urlpatterns = [
    path('', index_view, name='getphoto'),
    path('search/', search_photos, name='search'),
    path('detail/<str:id>/', detail_view, name='detail'),
]