from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(label=u'Заголовок', max_length=255)
    text = forms.CharField(label=u'Текст вопроса', widget=forms.Textarea)
    
    def __init__(self, user, **kwargs):
        self._user = user
        super(AskForm, self).__init__(**kwargs)
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidateError(u'Заголовок должен быть больше одного символа')
        
        return title
        
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidateError(u'Тект должен быть больше одного символа')
        
        return text
        
    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label=u'Ваш вопрос', widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
     
    def __init__(self, user, **kwargs):
        self._user = user
        super(AskForm, self).__init__(**kwargs)
         
    def clean(self):
        try:
            Ouestion.objects.get(id=self.cleaned_data.get('question'))
        except:
            raise ValidateError(u'Вопрос на который вы отвечаете не существует или удалён')
         
        return self.cleaned_data 
         
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidateError(u'Тект должен быть больше одного символа')
         
        return text
        
    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
	