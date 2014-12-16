from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
# from gics.models import Work, Anime, Rating, Page

"""class AnimeDetail(DetailView):
    model = Anime
    def get_context_data(self, **kwargs):
        context = super(AnimeDetail, self).get_context_data(**kwargs)
        context['object'].source = context['object'].source.split(',')[0]
        if self.request.user.is_authenticated():
            try:
                context['rating'] = self.object.rating_set.get(user=self.request.user).choice
            except Rating.DoesNotExist:
                pass
        return context

class AnimeList(ListView):
    model = Anime
    context_object_name = 'anime'
    def get_queryset(self):
        return Anime.objects.order_by('title') if self.kwargs['mode'] == 'z' else Anime.objects.all()
    def get_context_data(self, **kwargs):
        context = super(AnimeList, self).get_context_data(**kwargs)
        context['template_mode'] = 'work_no_poster.html' if self.kwargs['mode'] == 'a' else 'work_poster.html'
        if self.request.user.is_authenticated():
            for obj in context['object_list']:
                try:
                    obj.rating = obj.rating_set.get(user=self.request.user).choice
                except Rating.DoesNotExist:
                    pass
        return context 

class RatingList(ListView):
    model = Rating
    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        ordering = ['willsee', 'like', 'neutral', 'dislike', 'wontsee']
        context = super(RatingList, self).get_context_data(**kwargs)
        context['object_list'] = sorted(context['object_list'], key=lambda x: ordering.index(x.choice))
        return context"""

def index(request):
    return render(request, 'index.html')
