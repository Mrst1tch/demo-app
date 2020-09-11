import requests
from django.shortcuts import render
# Create your views here.


def getphoto(request):
    url = f'{BASE_URL}/photos'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    request_param = requests.get(url, params=params)
    request_param = request_param.json()

    return request_param