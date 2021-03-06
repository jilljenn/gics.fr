# coding=utf8
from django.db import models
from django.contrib.auth.models import User
from secret import MAIL_CHOICES


class UserProfile(models.Model):  # Garantir le lien
    user = models.OneToOneField(User)
    school = models.ForeignKey('School')
    school_year = models.CharField(max_length=32)
    newsletter = models.BooleanField(default=True)


class Person(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, blank=True, null=True)
    phone_number = models.CharField(max_length=64, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    mail = models.CharField(max_length=128)
    school = models.ForeignKey('School', blank=True, null=True)
    majors = models.ManyToManyField('Discipline', blank=True)
    status = models.CharField(max_length=15, default='speaker', choices=(
        ('member', 'Membre adhérent'),
        ('speaker', 'Simple intervenant'),
        ('former', 'Ancien membre ou intervenant')
    ))
    has_priority = models.BooleanField(default=False)
    favorite_schools = models.ManyToManyField('School', related_name='favorited', blank=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.first_name if not self.surname else '%s %s' % (self.first_name, self.surname)
    def get_name(self):
        return str(self)
    class Meta:
        ordering = ['first_name']
        verbose_name_plural = 'people'


class Note(models.Model):
    content = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


class UserHistory(models.Model):
    user = models.ForeignKey(Person)
    date = models.DateField()
    action = models.CharField(max_length=15, choices=(
        ('ping', 'Contacté(e)'),
        ('pong', 'A répondu'),
        ('joined', 'Adhésion'),
        ('quit', 'Démission'),
        ('fired', 'Radiation'),
        ('offered', 'Don')
    ))
    donation = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    school = models.ForeignKey('School', blank=True, null=True)
    def __str__(self):
        return '%s %s' % (self.user, self.action)
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "user histories"


class School(models.Model):
    title = models.CharField(max_length=64)
    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True)
    school_type = models.CharField(max_length=11, choices=(
        ('highschool', 'Lycée'),
        ('institution', 'Institution'),
    ), default='institution')
    picture = models.ForeignKey('Document', blank=True, null=True)
    def __str__(self):
        return self.title


class Discipline(models.Model):
    slug = models.SlugField(max_length=64)
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title


class Lecture(models.Model):
    discipline = models.ManyToManyField(Discipline, blank=True)  # Tags ou disciplines ?
    title = models.CharField(max_length=64)
    description = models.TextField()
    poster = models.CharField(max_length=32, default='', blank=True)
    links = models.TextField(default='', blank=True)
    def __str__(self):
        return self.title
    def get_discipline_slugs(self):
        slugs = []
        for discipline in self.discipline.all():
            slugs.append(discipline.slug)
        return ' ' + ' '.join(slugs)


class Session(models.Model):
    lecture = models.ForeignKey('Lecture')
    school = models.ForeignKey('School')
    date = models.DateTimeField()
    speaker = models.ForeignKey(Person)
    details = models.TextField(default='', blank=True)
    slot_defined = models.BooleanField(default=False)
    media_printed = models.BooleanField(default=False)
    feedback_collected = models.BooleanField(default=False)
    debrief_done = models.BooleanField(default=False)
    def __str__(self):
        return self.lecture.title

    class Meta:
        ordering = ['date']


class News(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    content = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "news"


class Page(models.Model):
    name = models.SlugField()
    markdown = models.TextField()
    def __str__(self):
        return self.name


class Document(models.Model):
    content = models.FileField(upload_to='files')
    def __str__(self):
        return self.content.name


class Question(models.Model):
    statement = models.CharField(max_length=512)
    answer = models.TextField()
    def __str__(self):
        return self.statement


def to_form(choices):
    return [(choice_id, choice_name) for choice_id, choice_name, _ in choices]


class Contact(models.Model):
    action = models.CharField(max_length=32, choices=to_form(MAIL_CHOICES), default='default', verbose_name='Que souhaitez-vous faire ?')
    name = models.CharField(max_length=128, verbose_name='Votre nom complet')
    email = models.CharField(max_length=128, verbose_name='Votre mail')
    message = models.TextField(verbose_name='Votre message')


class Alias(models.Model):
    slug = models.SlugField(unique=True)
    path = models.CharField(max_length=32)
