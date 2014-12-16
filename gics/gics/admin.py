# coding=utf8
from gics.models import School, Lecture, Session, UserHistory
from django.forms import Textarea
from django.db import models
from django.contrib import admin, messages

class SchoolAdmin(admin.ModelAdmin):
    pass

class UserHistoryAdmin(admin.ModelAdmin):
    pass

class LectureAdmin(admin.ModelAdmin):
    pass

class SessionAdmin(admin.ModelAdmin):
    pass

class DisciplineAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Discipline, DisciplineAdmin)
