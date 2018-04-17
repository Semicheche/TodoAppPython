# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todoapp/index.html'

    def get_queryset(self):
        return Task.objects.all()

class DetailView(generic.DetailView):
    model = Task
    template_name = 'todoapp/detail.html'