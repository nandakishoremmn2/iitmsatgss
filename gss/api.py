from tastypie import fields, utils
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.exceptions import Unauthorized

from gss.models import Telecommand, Attribute, Option


from django.contrib.auth.models import User
from django.db.models import Count

class OptionResource(ModelResource):
	class Meta:
		queryset = Option.objects.all()
		resource_name = 'option'
		authorization = Authorization()

class AttributeResource(ModelResource):
	options = fields.ToManyField(OptionResource, 'option_set', full=True)

	class Meta:
		queryset = Attribute.objects.all()
		resource_name = 'attribute'
		authorization = Authorization()

class TelecommandResource(ModelResource):
	attributes = fields.ToManyField(AttributeResource, 'attribute_set', full=True)

	class Meta:
		queryset = Telecommand.objects.all()
		max_limit = 0
		limit = 0
		excludes = ["author"]
		resource_name = 'telecommand'
		authorization = Authorization()