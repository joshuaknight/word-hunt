from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormMixin
from django.utils import timezone
from django.http import *

def home_page(request):
	a = Round3_answer.objects.all()
	a.delete()
	return render(request,'index.html')


class my_question(FormView):
	template_name = 'my_question_list.html'
	context_object_name = 'question_list'
	form_class = Myform

	def form_valid(self,form):		
		form.save()
		return super(my_question,self).form_valid(form)

	def get_success_url(self):
		return reverse('question')        

def list_my_view(request,pk):
	query = QuestionandAnswer.objects.get(pk = pk)
	try:
		i = query.id + 1
	except:
		pass
	if request.method == 'POST':	
		if request.POST['grp1']:
			if str(query.answer) == str(request.POST['grp1']):
				answer = 'Correct'
			else:
				answer = 'NotCorrect'				
			Quiz.objects.create(question = query.question_name,
				options = request.POST['grp1'],correct = answer)
	return render(request,'my_list.html',{'question_list' : query,'i' : i })

def score(request):
	query = Quiz.objects.filter(correct = 'Correct')
	Score = query.count()
	total = Quiz.objects.values_list('question').count()
	return render(request,'scoreboard.html',{'score' : Score,'total' : total})



def round3(request,pk):		
	if request.method == 'POST':	
		if request.POST['user_input']:
			x  = int(pk) - 1 
			result = Round3.objects.get(pk = x)
			if str(result.answer) == str(request.POST['user_input']):
				answer = 'Correct'
			else:
				answer = 'NotCorrect'								
			Round3_answer.objects.create(question = result.question,
			user_input = request.POST['user_input'],correct = answer)
	try:		
		form = Round3_answerForm
		query = Round3.objects.get(pk = pk)
		i = query.id + 1
		return render(request,'round3.html',{'question_list' : query,'i' : i ,'form':form })		
		
	except Round3.DoesNotExist:
		return HttpResponseRedirect('/score/round3')		
	



	
class AddRound3(FormView):
	template_name = 'form.html'
	form_class = Round3Form

	def form_valid(self,form):
		form.save()
		return super(AddRound3,self).form_valid(form)


	def get_success_url(self):
		return reverse('add_round3')



def score_round(request):
	query = Round3_answer.objects.filter(correct = 'Correct')
	Score = query.count()
	total = Round3_answer.objects.values_list('question').count()
	print Score 
	print total
	return render(request,'scoreboard.html',{'score' : Score,'total' : total})


