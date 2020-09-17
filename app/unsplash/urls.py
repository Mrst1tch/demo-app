from django.urls import path
from .views import index_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('detail/<str:id>/', detail_view, name='detail'),
]