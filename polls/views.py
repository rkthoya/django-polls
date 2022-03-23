from django.http import HttpResponse


def polls_app_index(request):
    return HttpResponse("Hello. You're at polls' index!")
