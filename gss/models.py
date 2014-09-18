from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100)
	parent_tag = models.ForeignKey('self', null=True, blank=True)

	def __unicode__(self):
		return self.name

class Remark(models.Model):
	remark = models.TextField()
	cleared = models.BooleanField(default=False)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.remark

class Question(models.Model):
	question = models.TextField()
	author = models.ForeignKey(User, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	detailed_answer = models.TextField(default="ans")
	approved_by = models.ManyToManyField(User, related_name='approver', blank=True)
	locked = models.BooleanField(default=False)
	created_on = models.DateField(auto_now_add=True)
	last_modified = models.DateField(auto_now=True)
	remarks = models.ManyToManyField(Remark, blank=True)

	TEST = '0'
	PRACTICE = '1'
	TEST_TYPE_CHOICES = (
		(TEST, 'Test'),
		(PRACTICE, 'Practice'),
	)
	type = models.CharField(
		max_length=1,
		choices=TEST_TYPE_CHOICES,
		default=TEST
	)

	EASY = '0'
	MEDIUM = '1'
	HARD = '2'
	DIFFICULTY_CHOICES = (
		(EASY, 'Easy'),
		(MEDIUM, 'Medium'),
		(HARD, 'Hard'),
	)
	difficulty = models.CharField(
		max_length=1,
		choices=DIFFICULTY_CHOICES,
		default=MEDIUM
	)

	def is_approved(self):
		return self.approved_by.count() > 0

	def __unicode__(self):
		return "(" + str(self.author) + ")-> " +  (self.question[:50] + '...' if len(self.question) > 50 else self.question)

class Answer(models.Model):
	answer = models.CharField(max_length=150, default="1")
	question = models.ForeignKey(Question)
	correct_answer = models.BooleanField(default=False)
	answerd_by = models.IntegerField(default=0)

	def __unicode__(self):
		return self.answer