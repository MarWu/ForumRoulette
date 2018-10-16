from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("You're at the posts index.")


def post(request, id, post_title):
    return HttpResponse("You're looking at post Nr: %i with title %s" % id, post_title)
