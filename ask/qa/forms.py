from django import forms
from django.core.exceptions import ValidationError
from qa.models import Question, Answer
from django.contrib.auth.models import User

def getTestUser():
    try:
        user_ = User.objects.get(username='test_user')
    except:
        user_ = User.objects.create_user('test_user', None, 'test_user')
        user_.save()
    return user_


class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255, min_length = 1)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea, min_length = 1)
    
    def __init__(self, **kwargs):
        self.user_ = getTestUser() 
        super(AskForm, self).__init__(kwargs)
        
    def save(self):
        self.cleaned_data['author'] = self.user_
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label='Ваш ответ', widget=forms.Textarea, min_length = 1)
    question = forms.ModelChoiceField(queryset=Question.objects, widget=forms.HiddenInput)
     
    def __init__(self, **kwargs):
        self.user_ = getTestUser()      
        super(AnswerForm, self).__init__(kwargs)
     
        
    def save(self):
        self.cleaned_data['author'] = self.user_
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
