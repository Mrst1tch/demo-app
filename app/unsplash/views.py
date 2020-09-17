import requests
from django.conf import settings
from django.shortcuts import render


# Create your views here.

BASE_URL = 'https://api.unsplash.com/'

def getphoto():
    url = f'{BASE_URL}/photos/random'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    response = response.json()

    return response

def detail_photo_url(id_photo):
    url = f'{BASE_URL}/photos/{id_photo}'
    params = {
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    response = response.json()
    return response

def detail_view(request, id):
    response = detail_photo_url(id)
    context = {
        'response': response
    }
    return render(request, 'detail.html', context)


    