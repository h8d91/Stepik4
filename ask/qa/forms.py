from django import forms

class AskForm(forms.Form):
	title = forms.CharField(label='���������', max_length=255)
	text = form.TextField(label='����� �������', widget=forms.TextArea)
	
	def clean(self):
		return True
	
	def clean_title(self):
		if len(self.title) < 2:
			raise ValidateError(u'��������� ������ ���� ������ ������ �������')
		
		return self.title
	
	def clean_text(self):
		if len(self.text) < 2:
			raise ValidateError(u'���� ������ ���� ������ ������ �������')
		
		return self.text
	
	def save(self):
		question = Question(title=self.title, text=self.text)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = form.TextField(label='��� ������', widget=forms.TextArea)
	question = form.IntegerField(visible=False)
	
	def clean(self):
		try:
			Ouestion.objects.get(id=self.question)
		except:
			raise ValidateError(u'������ �� ������� �� ��������� �� ���������� ��� �����')
		
		return True 
	
	def clean_text(self):
		if len(self.text) < 2:
			raise ValidateError(u'���� ������ ���� ������ ������ �������')
		
		return self.text
		
	def save(self):
		answer = Answer(text=self.text, question=self.question)
		answer.save()
		return answer
	