from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


def profile(request, username):
    return HttpResponse("You're looking at user %s." % username)
