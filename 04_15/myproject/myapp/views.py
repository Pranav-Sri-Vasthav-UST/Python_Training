from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is my first Django web app!")

def info(request):
    return HttpResponse("kuu ku ku ku ku kooo")