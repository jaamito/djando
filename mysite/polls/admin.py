from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
   list_display = ('question_text', 'pub_date','wa_published_recently')
   fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
   inclines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
