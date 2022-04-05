from django.http import HttpResponse


def index(request):
    return HttpResponse("IGS Employee API. It works.")