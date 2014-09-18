from django.contrib import admin
from gss.models import Telecommand, Attribute, Option

class OptionsInline(admin.TabularInline):
	model = Option
	extra = 1

class AttributesInline(admin.StackedInline):
	inlines = [OptionsInline]
	model = Attribute
	extra = 1

class AttributeAdmin(admin.ModelAdmin):
	inlines = [OptionsInline]
	model = Attribute

class TelecommandAdmin(admin.ModelAdmin):
	inlines = [AttributesInline]
	list_filter = ('author', 'created_on', 'last_modified')
	model = Telecommand

admin.site.register(Telecommand, TelecommandAdmin)
admin.site.register(Attribute, AttributeAdmin)