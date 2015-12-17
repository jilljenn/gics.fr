# coding=utf8
from gics.models import School, Lecture, Session, UserHistory, Discipline, News, Page, Document, Person, Question, Note
from django.forms import Textarea
from django.db import models
from django.contrib import admin, messages
from pagedown.widgets import AdminPagedownWidget

class SessionInline(admin.TabularInline):
    model = Session

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'manager', 'school_type']
    list_filter = ['school_type']
    actions = ['make_highschool', 'make_institution']

    def make_highschool(self, request, queryset):
        rows_updated = queryset.update(school_type='highschool')
        if rows_updated == 1:
            message_bit = "1 établissement a"
        else:
            message_bit = "%s établissements ont" % rows_updated
        self.message_user(request, "%s été mis à jour." % message_bit)
    make_highschool.short_description = "Changer le type en lycée"

    def make_institution(self, request, queryset):
        rows_updated = queryset.update(school_type='institution')
        if rows_updated == 1:
            message_bit = "1 établissement a"
        else:
            message_bit = "%s établissements ont" % rows_updated
        self.message_user(request, "%s été mis à jour." % message_bit)
    make_institution.short_description = "Changer le type en institution"

    inlines = [SessionInline,]

class UserHistoryInline(admin.TabularInline):
    model = UserHistory

class PersonAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'mail', 'phone_number', 'comments', 'is_speaker']
    list_filter = ['is_speaker']
    inlines = [UserHistoryInline,]

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
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

class DocumentAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Note, NoteAdmin)
