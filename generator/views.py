from django.shortcuts import render
from django.http import HttpResponse

import random


def home(request):
    return render(request, 'generator/home.html', {'password': "gerrard8*"})

def description(request):
    return render(request, "generator/description.html")


def password(request):
    thepassword = ""
    characters = list("abcdefghijklnoprstquwvxyz")
    length=int(request.GET.get('length', 12))
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIOPRSTQUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()-+"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))


    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword })
