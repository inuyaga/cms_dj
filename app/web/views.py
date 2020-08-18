from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class webindex(TemplateView):
    template_name = "web/index.html"
    
class historia(TemplateView):
    template_name = "web/historia.html"