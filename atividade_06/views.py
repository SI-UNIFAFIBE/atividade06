from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):
    return HttpResponse("Ola mundo!")


def starter(request):
    r = requests.get('https://randomuser.me/api/')
    jsonData = json.loads(r.text)

    context = {"user": jsonData["results"][0]}

    print(context)

    return render(request, "atividade06/starter.html", context)
