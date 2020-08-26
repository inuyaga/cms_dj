from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from app.cucm.form import ProspectoForm
from app.sie.models import Prospecto
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = "cucm/inicio.html"

class InscripcionCucmView(CreateView):
    model = Prospecto
    form_class = ProspectoForm
    template_name = "cucm/inscripcion.html"
    success_url = reverse_lazy('index')