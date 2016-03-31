from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required

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
                'answerform': AnswerForm(question_id = question.id, text = 'Ваш ответ'),
        })
        
#@login_required
def answer(request):
        if request.method == 'POST':
            answer = AnswerForm(**request.POST.dict())
            
            if answer.is_valid(): 
                answer.save()
            
            try:
                question = Question.objects.get(id = int(answer.cleaned_data['question_id']))
            except:
                raise Http404

            return HttpResponseRedirect(question.get_url())
        
        raise Http404
            		

#@login_required
def ask(request):
        if request.method == 'POST':
            question = AskForm(**request.POST.dict())
            if question.is_valid():
                question = question.save()
                return HttpResponseRedirect(question.get_url())		
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
                'questions': page,
                'paginator': paginator,
                'page': page,
        })
