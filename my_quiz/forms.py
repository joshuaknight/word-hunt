from django import forms
from django.forms import ModelForm,Textarea
from .models import *


class Myform(ModelForm):
	class Meta:
		model = QuestionandAnswer
		fields = '__all__'
		widgets = {
			'question_name' : forms.Textarea(attrs = {'rows':5,'cols':5})
		}

class quizform(ModelForm):
	class Meta:
		model =  Quiz
		fields = ('options',)		
			
		widgets = {
			'options' : forms.RadioSelect(choices = '')#{(1,op1),(2,op2),(3,op3),(4,op4)})
		}

class Round3Form(ModelForm):
	class Meta:
		model = Round3
		fields = '__all__'


class Round3_answerForm(ModelForm):
	class Meta:
		model = Round3_answer
		fields = '__all__'
		exclude = ('question','correct',)

		help_texts = {
			'user_input' : 'First Letter Must Be a Capital Letter'
		}