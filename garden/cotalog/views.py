from django.shortcuts import render
from django.views.generic import ListView
from cotalog.models import Plant



class PlantsView(ListView):
    model = Plant
    template_name = 'index.html'
