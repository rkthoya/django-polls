from django.http import HttpResponse


def site_index(request):
    return HttpResponse("Hi. Welcome to our site!")
