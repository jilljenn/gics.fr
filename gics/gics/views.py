# coding=utf-8
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from gics.models import News, Session, Page, School, Session, Lecture, Question, Discipline, Note, Person
from datetime import datetime
from markdown import markdown
import re

def index(request):
    return render(request, 'index.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

def contact(request):
    if request.POST:
        from_mail = request.POST.get('email')
        send_mail('[Contact] GICS', '%s <%s> a envoyé un message via le site :\n\n%s' % (request.POST.get('name'), from_mail, request.POST.get('message')), from_mail, ['vie@jill-jenn.net'], fail_silently=True)
    return render(request, 'contact.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

def register(request):
    context = {}
    if request.POST:
        contacts = request.POST.get('contacts').strip().split('\n')
        re_mail = re.compile(r'\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})\b')
        re_name = re.compile(r'([^ ]+) +$')
        re_number = re.compile(r'([0-9]{2}[\. ]?[0-9]{2}[\. ]?[0-9]{2}[\. ]?[0-9]{2}[\. ]?[0-9]{2})')
        added_contacts = []
        errors = []
        for line in contacts:
            Note(content=line).save()
            contact = {}
            has_mail = re_mail.search(line)
            if has_mail:
                contact['mail'] = has_mail.group(1)
                first, second = line.split(contact['mail'])
                has_number = re_number.search(second)
                if has_number:
                    contact['phone_number'] = has_number.group(1)
                    contact['comments'] = second.replace(contact['phone_number'], '').strip()
                else:
                    has_number = re_number.search(first)
                    if has_number:
                        contact['phone_number'] = has_number.group(1)
                        contact['comments'] = second.strip()
                        first = first.replace(contact['phone_number'], '')
            else:
                has_number = re_number.search(line)
                if has_number:
                    contact['phone_number'] = has_number.group(1)
                    first, second = line.split(contact['phone_number'])
                    contact['comments'] = second.strip()
                else:
                    errors.append(line)
                    continue  # I give up with this line (couldn't find either mail or phone number)
            has_name = re_name.search(first)
            if has_name:
                name = has_name.group(1)
                remainder = first.replace(name, '').strip()
                if remainder:
                    contact['first_name'] = remainder
                    contact['surname'] = name
                else:
                    contact['first_name'] = name
            Person(**contact).save()
            full_name = ('%s %s' % (contact['first_name'], contact.get('surname', ''))).strip()
            added_contacts.append(full_name)
        context['message'] = u'Contacts ajoutés (%d) :<br />' % len(added_contacts)
        for name in added_contacts:
            context['message'] += '- %s<br />' % name
        if errors:
            print(errors)
            context['message'] += '<br />Erreur pour les lignes suivantes (%d) :<br />' % (len(errors))
            for line in errors:
                context['message'] += '- %s<br />' % line
    return render(request, 'register.html', context)

def faq(request):
    return render(request, 'faq.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

def forum(request):
    return render(request, 'forum.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

class MarkdownView(DetailView):
    model = Page
    slug_field = 'name'
    template_name = 'static.html'
    """def get_object(self):
        try:
            return super(MarkdownView, self).get_object()
        except Http404:
            Page(name=self.kwargs['slug'], markdown='').save()  # Create the page if it does not exist
            raise Http404"""
    def get_context_data(self, **kwargs):
        page = super(MarkdownView, self).get_object()
        return {'html': markdown(page.markdown), 'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]}

class SchoolList(ListView):
    model = School

class SchoolDetail(DetailView):
    model = School

class SessionList(ListView):
    model = Session

class LectureList(ListView):
    model = Lecture
    def get_queryset(self):
        return super(LectureList, self).get_queryset().order_by('title')
    def get_context_data(self, **kwargs):
        context = super(LectureList, self).get_context_data()
        context['disciplines'] = Discipline.objects.all()
        return context

class LectureDetail(DetailView):
    model = Lecture

class NewsList(ListView):
    model = News
    def get_queryset(self):
        return super(NewsList, self).get_queryset().order_by('-date')

class NewsDetail(DetailView):
    model = News

class QuestionList(ListView):
    model = Question

class DisciplineDetail(DetailView):
    model = Discipline
