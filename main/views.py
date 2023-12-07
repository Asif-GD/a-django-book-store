from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(response):
    return HttpResponse("<h1>Welcome to the book-store!</h1>")


def search(response):
    return HttpResponse("<h1>Your search results below.</h1>")
