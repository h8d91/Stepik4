from django.http import HttpResponse, HttpRequest, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from django.shortcuts import render
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
        return HttpResponse('OK')

def login(request, *args, **kwargs):
        return test(request, args, kwargs)

def signup(request, *args, **kwargs):
        return test(request, args, kwargs)

def question(request, *args, **kwargs):
        try:
            qid = int(kwargs['id'])
            question = Question.objects.get(id = qid)
        except:
            raise Http404
        
        answers = Answer.objects.filter(question = question).order_by('-added_at').all()[:]
        
        return render(request, 'question.html', {
                'answers': answers,
                'question': question,
        })

def ask(request, *args, **kwargs):
		if request.method == 'POST':
			question = AskForm(request.POST)
			if question.is_valid:
				question.save()
				return HttpResponseRedirect(question.qet_url())		
		else:
			question = AskForm()
			
		return render(request, 'ask.html', {
					'question': question,
			})		

def popular(request):
        questions = Question.objects.order_by('-rating', '-added_at')
        
        limit = 10
        
        try:
            pagenum = int(request.GET.get('page', 1))
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
            pagenum = int(request.GET.get('page', 1))
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
