# coding=utf8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):  # Garantir le lien
    user = models.OneToOneField(User)
    school = models.ForeignKey('School')
    school_year = models.CharField(max_length=32)
    newsletter = models.BooleanField()

class Phantom(models.Model):
    name = models.CharField(max_length=64)

class UserHistory(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    action = models.CharField(max_length=15, choices=(
        ('joined', 'Adhésion'),
        ('quit', 'Démission'),
        ('fired', 'Radiation'),
        ('offered', 'Don'),
    ))
    donation = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    def __unicode__(self):
        return '%s %s' % (self.user, self.action)

class School(models.Model):
    title = models.CharField(max_length=64)
    address = models.TextField()
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=32)
    manager = models.ForeignKey(User)
    def __unicode__(self):
        return self.title

class Discipline(models.Model):
    title = models.CharField(max_length=64)
    def __unicode__(self):
        return self.title

class Lecture(models.Model):
    discipline = models.ManyToManyField(Discipline)  # Tags ou disciplines ?
    title = models.CharField(max_length=32)
    description = models.TextField()
    poster = models.CharField(max_length=32, default='', blank=True)
    links = models.TextField(max_length=168, default='')
    def __unicode__(self):
        return self.title

class Session(models.Model):
    lecture = models.ForeignKey('Lecture')
    school = models.ForeignKey('School')
    date = models.DateTimeField()
    speaker = models.ForeignKey(User)
    details = models.TextField(default='', blank=True)
    slot_defined = models.BooleanField(default=False)
    media_printed = models.BooleanField(default=False)
    feedback_collected = models.BooleanField(default=False)
    debrief_done = models.BooleanField(default=False)
    def __unicode__(self):
        return self.lecture.title

class News(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    content = models.TextField()
    def __unicode__(self):
        return self.title

class Page(models.Model):
    name = models.SlugField()
    markdown = models.TextField()
    def __unicode__(self):
        return self.name

class Document(models.Model):
    content = models.FileField(upload_to='files')
    def __unicode__(self):
        return self.content.name
