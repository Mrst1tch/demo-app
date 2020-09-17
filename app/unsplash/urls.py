from django.urls import path
from .views import index_view, search_view, detail_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('admin/', detail_view, name='detail'),
    path('detail/<str:id>/', detail_view, name='detail'),


]