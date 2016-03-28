from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(label=u'Заголовок', max_length=255)
    text = forms.CharField(label=u'Текст вопроса', widget=forms.TextInput)
    
    def clean(self):
        return True
    
    def clean_title(self):
        if len(self.title) < 2:
            raise ValidateError(u'Заголовок должен быть больше одного символа')

        return self.title

    def clean_text(self):
        if len(self.text) < 2:
            raise ValidateError(u'Тект должен быть больше одного символа')

        return self.text

    def save(self):
        question = Question()
        question.title = self.cleaned_data['title']
        question.text = self.cleaned_data['text']
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label=u'Ваш вопрос', widget=forms.TextInput)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        try:
            Ouestion.objects.get(id=self.question)
        except:
            raise ValidateError(u'Вопрос на который вы отвечаете не существует или удалён')

        return True 

    def clean_text(self):
        if len(self.text) < 2:
            raise ValidateError(u'Тект должен быть больше одного символа')

        return self.text

    def save(self):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.question = self.cleaned_data['question']
        answer.save()
        return answer
	