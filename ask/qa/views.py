from django.http import HttpResponse, HttpRequest, Http404

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def http404():
	raise Http404

def login(request, *args, **kwargs):
	return http404()

def signup(request, *args, **kwargs):
        return http404()

def question(request, *args, **kwargs):
        return HttpResponse(request.get_full_path())

def ask(request, *args, **kwargs):
        return http404()

def popular(request, *args, **kwargs):
        return http404()

def new(request, *args, **kwargs):
        return http404()

def home(request, *args, **kwargs):
        return http404()


