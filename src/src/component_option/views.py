from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from .models import Categorie, ManufacturingFirm

from .forms import CategorieCreateForm, ManufacturingFirmCreateForm

# Create your views here.


class CategorieListView(ListView):
    model = Categorie

    template_name = "list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['href'] = 'categorie'
        return context

class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieCreateForm
    template_name = "create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['action'] = 'Создание нового объекта'
        return context

class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieCreateForm
    template_name = "create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['action'] = 'Редактирование объекта'
        return context

class CategorieDeleteView(DeleteView):
    model = Categorie
    success_url = '/categorie/list'
    template_name = "delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context



class ManufacturingFirmListView(ListView):
    model = ManufacturingFirm

    template_name = "list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фирма производитель'
        context['href'] = 'manufirm'
        return context

class ManufacturingFirmCreateView(CreateView):
    model = ManufacturingFirm
    form_class = ManufacturingFirmCreateForm
    template_name = "create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фирма производитель'
        context['action'] = 'Создание нового объекта'
        return context

class ManufacturingFirmUpdateView(UpdateView):
    model = ManufacturingFirm
    form_class = ManufacturingFirmCreateForm
    template_name = "create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фирма производитель'
        context['action'] = 'Редактирование объекта'
        return context

class ManufacturingFirmDeleteView(DeleteView):
    model = ManufacturingFirm
    success_url = '/manufirm/list'
    template_name = "delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фирма производитель'
        return context

class ManufacturingFirmDetailView(DetailView):
    model = ManufacturingFirm
    template_name = "detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фирма производитель'
        return context
