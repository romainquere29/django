from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return HttpResponse('This is the generator homepage')
    return render(request, 'generator/home.html', {'password':'sqlkdh21852SGSD', "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],"dogsname" : ["djambo","pluto"],"numbers" : range(8,14)})

def password(request):
    #return HttpResponse('This is the generator homepage')
    my_password = ''
    characters = list('azertyuiopqsdfghjklmwxcvbn')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('AZERTYUIOPQSDFGHJKLMWXCVBN'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('specials'):
        characters.extend(list('&é-è_çà^$*ù!:,~#|^@'))
    for occurence in range(length):
        my_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password':my_password})

def about(request):
    return render(request, 'generator/about.html', {'creator':'Romain QUERE'})
