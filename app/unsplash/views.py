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
    response = get_random_photos()

    search_value = request.GET.get('query', None)
    response = search_photo_url(search_value)
    context = {
        'response': response,
        'search_form': search_form
    }
    return render(request , 'unsplash/search.html' , context)


def save_photos(request):
    if request.user.is_authenticated:
        author = response['user']['name']
        image = response['urls']['small']
        id_photo = response['id']
        data  = {
            'author':author,
            'image': image,
            'id_photo': id_photo,
        }
        photo_object= Photo.objects.create(**photo_data)
        photo_object.users.add(request.user)
        return messages.success(request, f'Photo is saved!')


def detail_photo_url(id_photo):
    #if kwargs.get('q', None):
    url = f'{BASE_URL}/photos/{id_photo}'
    params = {
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

        
def index_view(request):
    search_form = SearchPhoto()
    if request.method == 'GET':
        search_form = SearchPhoto(request.GET)
    if request.method == 'POST': 
        response = response[photo_number]
    response = get_random_photos()
    context = {
        'response': response,
        'search_form': search_form
    }
    return render(request, 'unsplash/index.html', context)        


def detail_view(request, id):
    response = detail_photo_url(id)
    context = {
        'response': response
    }
    if request.method == 'POST': 
        save_photos(request)
    return render(request, 'unsplash/detail.html', context)




class SearchPhoto(forms.Form):
    query = forms.CharField(max_length=80, required=False)
    