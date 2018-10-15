from django.http import HttpResponse
from django.shortcuts import render


def profile(request, username):
    return HttpResponse("You're looking at user %s." % username)
