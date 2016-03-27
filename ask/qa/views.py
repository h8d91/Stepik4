from django.http import HttpResponse, HttpRequest, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from django.shortcuts import render
from django.core.urlresolvers import reverse

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

def popular(request):
        questions = Question.objects.order_by('-rating', '-added_at')
        
        limit = 10
        
        try:
            pagenum = int(request.GET.get('page'))
        except:
            raise Http404
        
        paginator = Paginator(questions, limit)
        paginator.baseurl = reverse('popular') + '?page='
        
        try:
            page = paginator.page(pagenum)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        return render(request, 'popular.html', {
                'questions': page.object_list,
                'paginator': paginator,
                'page': page,
        })

def new(request, *args, **kwargs):
        return test(request, args, kwargs)

def home(request):
        questions = Question.objects.order_by('-added_at')
        limit = 10
        
        try:
            pagenum = int(request.GET.get('page'))
        except:
            raise Http404
        
        paginator = Paginator(questions, limit)
        paginator.baseurl = reverse('home') + '?page='
        
        try:
            page = paginator.page(pagenum)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        return render(request, 'main_page.html', {
                'questions': page.object_list,
                'paginator': paginator,
                'page': page,
        })
