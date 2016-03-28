from django import forms

class AskForm(forms.Form):
	title = forms.CharField(label='Заголовок', max_length=255)
	text = form.TextField(label='Текст вопроса', widget=forms.TextArea)
	
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
		question = Question(title=self.title, text=self.text)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = form.TextField(label='Ваш вопрос', widget=forms.TextArea)
	question = form.IntegerField(visible=False)
	
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
		answer = Answer(text=self.text, question=self.question)
		answer.save()
		return answer
	