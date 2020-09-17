import requests
from django.shortcuts import render
from django.conf import settings

# Create your views here.

BASE_URL = 'https://api.unsplash.com/'

def getphoto():
    url = f'{BASE_URL}/photos'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    request_param = requests.get(url, params=params)
    request_param = request_param.json()

    return request_param

    def detail_photo_url(id_photo):
        url = f'{BASE_URL}/photos/{id_photo}'
    params = {
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response_param = requests.get(url, params=params)
    response_param = response_param.json()
    return response_param


    def detail_view(request, id):
        response_param = detail_photo_url(id)
    context = {
        'response': response_param
    }
    return render(request, 'detail.html', context)