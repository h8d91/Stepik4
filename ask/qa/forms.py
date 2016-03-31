from django import forms
from django.core.exceptions import ValidationError
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)
    
    def __init__(self, **kwargs):
        #self._user = user
        try:
            self.user_ = User.objects.get(username='test_user')
        except:
            self.user_ = User.objects.create_user('test_user', None, 'test_user')
            self.user_.save()
        super(AskForm, self).__init__(kwargs)
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть больше одного символа')
        
        return title
        
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 2:
            raise ValidationError('Тект должен быть больше одного символа')
        
        return text
        
    def save(self):
        self.cleaned_data['author'] = self.user_
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label='Ваш ответ', widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
     
    def __init__(self, **kwargs):
        #self._user = user
        try:
            self.user_ = User.objects.get(username='test_user')
        except:
            self.user_ = User.objects.create_user('test_user', None, 'test_user')
            self.user_.save()
        super(AnswerForm, self).__init__(kwargs)
         
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 2:
            raise ValidationError('Тект должен быть больше одного символа')
         
        return text

    def clean_question(self):
        try:
            qid = int(self.cleaned_data['question'])
            #question = Ouestion.objects.get(id = qid)
        except:
            raise ValidationError('Вопрос на который вы отвечаете не существует или удалён')
         
        return qid 
        
    def save(self):
        self.cleaned_data['author'] = self.user_
        self.cleaned_data['question_id'] = self.cleaned_data['question']
        del self.cleaned_data['question_id']
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
