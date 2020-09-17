from django.urls import path
from .views import  detail_view

urlpatterns = [
    path('detail/<str:id>/', detail_view, name='detail'),
]