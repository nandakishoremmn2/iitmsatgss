from django.db import models
from django.contrib.auth.models import User

class Telecommand(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	author = models.ForeignKey(User)
	created_on = models.DateField(auto_now_add=True)
	last_modified = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.name

TEXT_INPUT = '0'
DROP_DOWN = '1'
RADIO = '2'
ATTR_TYPE_CHOICES = (
	(TEXT_INPUT, 'Text Input'),
	(DROP_DOWN, 'Drop Down'),
	(RADIO, 'Radio'),
)

class Attribute(models.Model):
	telecommand = models.ForeignKey(Telecommand, null=True, blank=True)
	
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

	fixed = models.BooleanField(default=False)

	type = models.CharField(
		max_length=2,
		choices=ATTR_TYPE_CHOICES,
		default=TEXT_INPUT
	)

	selected_option = models.OneToOneField('gss.Option',
		related_name="selected_option",
		null=True,
		blank=True,
		help_text='Use this only if attribute type is radio or dropdown'
	)

	def __unicode__(self):
		return self.name

class Option(models.Model):
	attribute = models.ForeignKey(Attribute, null=True, blank=True)
	
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200, null=True)
