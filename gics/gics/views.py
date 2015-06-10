from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from gics.models import News, Session, Page, School, Session, Lecture, Question, Discipline
from datetime import datetime
from markdown import markdown

def index(request):
    return render(request, 'index.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

def contact(request):
    return render(request, 'contact.html', {
        'news_list': News.objects.order_by('-date')[:5],
        'next_sessions': Session.objects.filter(date__gt=datetime.now()).order_by('date')[:5]
    })

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
