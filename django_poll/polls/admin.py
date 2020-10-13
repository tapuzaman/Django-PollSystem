from django.contrib import admin

from .models import Question, Answer

admin.site.site_header = "Admin Site"
admin.site.site_title = "Unlimited Power"
admin.site.index_title = "Welcome to the admin area"


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)