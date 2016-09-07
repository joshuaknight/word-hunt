from __future__ import unicode_literals
from django.db import models


class QuestionandAnswer(models.Model):
	question_name = models.CharField(max_length = 300)
	op1 = models.CharField(max_length = 100)
	op2 = models.CharField(max_length = 100)
	op3 = models.CharField(max_length = 100)
	op4 = models.CharField(max_length = 100)
	answer = models.IntegerField()

	def __unicode__(self):
		return self.question_name
		
class Quiz(models.Model):
	question = models.CharField(max_length=300)
	options = models.CharField(max_length = 100)
	correct = models.CharField(max_length=100)

class Round3(models.Model):
	question = models.CharField(max_length = 100)
	answer = models.CharField(max_length = 100)

class Round3_answer(models.Model):
	question = models.CharField(max_length = 200)
	user_input = models.CharField(max_length = 200,verbose_name = 'Answer',blank = True)
	correct = models.CharField(max_length = 200)





