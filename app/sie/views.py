from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from app.sie.forms import createAdmisionForm
from app.sie.models import Prospecto
# Create your views here.
class index(TemplateView):
    template_name = "sie/index.html"


class CreateAdmisiones(CreateView):
    model = Prospecto
    form_class = createAdmisionForm
    template_name = "sie/admisiones/registrar.html"
    success_url = reverse_lazy("sie:index")

class AdmisionesListView(ListView):
    model = Prospecto
    template_name = "sie/admisiones/index.html"


class AdmisionesDetailView(DetailView):
    model = Prospecto
    template_name = "sie/admisiones/detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['usuario'] = self.request.user
        return context


