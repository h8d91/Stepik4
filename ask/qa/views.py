from django.http import HttpResponse, Http404


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def http404():
	raise Http404

def login(request, *args, **kwargs):
	return http404()

def signup(request, *args, **kwargs):
        return http404()

def question(request, *args, **kwargs):
        return test(request, args, kwargs)

def ask(request, *args, **kwargs):
        return http404()

def popular(request, *args, **kwargs):
        return http404()

def new(request, *args, **kwargs):
        return http404()

def home(request, *args, **kwargs):
        return http404()


