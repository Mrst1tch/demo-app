import requests
from django.conf import settings
from django.shortcuts import render
from django.http.response import HttpResponse
from django import forms



# Create your views here.

BASE_URL = 'https://api.unsplash.com/'

def get_random_photos():
    url = f'{BASE_URL}/photos/random'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def get_photos(request):
    photos = get_random_photos()

    context = {
        'photos': photos
    }

    return render(request, 'unsplash/index.html', context)


def search_photo_url(search_data):
    url = f'{BASE_URL}search/photos'
    params = {
        'query':search_data,
        'client_id':settings.UNSPLASH_ACCESS_KEY,
        'per_page' : 10
    }
    response = requests.get(url, params=params)
    return response.json()

def search_photos(request):
    search_form = SearchPhoto()
    if request.method == 'GET':
        search_form = SearchPhoto(request.GET)
    else:
        search_form = ''
    response = get_photos(request)

    search_value = request.GET.get('query', None)
    response = search_photo_url(search_value)
    context = {
        'response': response,
        'search_form': search_form
    }
    return render(request , 'unsplash/search.html' , context)

def detail_photo_url(request):
    #if kwargs.get('q', None):
    url = f'{BASE_URL}/photos/{id_photo}'
    params = {
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    response = response.json()
    return response

        
        


class SearchPhoto(forms.Form):
    query = forms.CharField(max_length=80, label='Search Photo', required=False)
    