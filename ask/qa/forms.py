from django import forms
from django.core.exceptions import ValidationError
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
    
    def save(self):
        self.cleaned_data['author'] = self.user
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(label='Ваш ответ', widget=forms.Textarea, min_length = 1)
    question = forms.ModelChoiceField(queryset=Question.objects, empty_label=None, widget=forms.HiddenInput)
        
    def save(self):
        self.cleaned_data['author'] = self.user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(label='Логин', min_length = 3, max_length=255)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='Пароль', min_length = 6, max_length=255, widget=forms.PasswordInput)  
    
    def clean(self):
        try:
            user = User.objects.get(username = self.cleaned_data['username'])
        
            if user is not None:
                raise ValidationError('Не правильный логин или пароль')
        except User.DoesNotExist:       
            return self.cleaned_data
    
    def save(self, request):
        logout(request)       
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        user.save()
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        login(request, user)
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', min_length = 3, max_length=255)
    password = forms.CharField(label='Пароль', min_length = 6, max_length=255, widget=forms.PasswordInput)  
    
    def clean(self):       
        try:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            
            self.user_ =  authenticate(username = username, password = password)
        
            if self.user_ is None:
                raise ValidationError('Не правильный логин или пароль')
        except:
            raise ValidationError('Не правильный логин или пароль')
         
        return self.cleaned_data
     
    def save(self, request):
        logout(request)
        login(request, self.user_)
        return self.user_

    