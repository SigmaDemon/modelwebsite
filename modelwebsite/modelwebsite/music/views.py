from django.http import HttpResponse


def index():
    return HttpResponse('<h1>Welcome to the Music App Homepage')
