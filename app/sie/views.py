from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class index(TemplateView):
    template_name = "sie/index.html"