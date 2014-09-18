from django.contrib import admin
from gss.models import Question, Tag, Answer

class TagsInline(admin.TabularInline):
	model = Tag
	extra = 5

class TagAdmin(admin.ModelAdmin):
	fields = ['name', 'parent_tag']
	inlines = [TagsInline]	

class AnswersInline(admin.TabularInline):
	model = Answer
	extra = 5

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswersInline]
	list_display = ('__unicode__', 'created_on', 'is_approved')
	list_filter = ('author', 'created_on', 'tags')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Answer)