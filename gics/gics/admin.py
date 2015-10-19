# coding=utf8
from gics.models import School, Lecture, Session, UserHistory, Discipline, News, Page, Document, Person, Question, Note
from django.forms import Textarea
from django.db import models
from django.contrib import admin, messages

class SessionInline(admin.TabularInline):
    model = Session

class SchoolAdmin(admin.ModelAdmin):
    inlines = [SessionInline,]

class UserHistoryAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'mail', 'phone_number', 'comments')

class LectureAdmin(admin.ModelAdmin):
    pass

class SessionAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'school', 'speaker', 'date', 'slot_defined', 'media_printed', 'feedback_collected', 'debrief_done')
    def get_queryset(self, request):
        qs = super(SessionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(school__manager=request.user)

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class NewsAdmin(admin.ModelAdmin):
    pass

class PageAdmin(admin.ModelAdmin):
    pass

class DocumentAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Note, NoteAdmin)
