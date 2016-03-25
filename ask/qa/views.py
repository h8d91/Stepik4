from django.http import HttpResponse, HttpRequest

def test(request, *args, **kwargs):
        return HttpResponse('OK')

def login(request, *args, **kwargs):
        return test(request, args, kwargs)

def signup(request, *args, **kwargs):
        return test(request, args, kwargs)

def question(request, *args, **kwargs):
        return test(request, args, kwargs)

def ask(request, *args, **kwargs):
        return test(request, args, kwargs)

def popular(request, *args, **kwargs):
        return test(request, args, kwargs)

def new(request, *args, **kwargs):
        return test(request, args, kwargs)

def home(request, *args, **kwargs):
        return test(request, args, kwargs)


