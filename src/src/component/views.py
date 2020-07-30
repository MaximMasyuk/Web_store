from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView


from .models import Component

from .forms import ComponentCreateForm
# Create your views here.
class ComponentListView(ListView):
    model = Component

    template_name = "list_b.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        context['href'] = 'component'
        return context

class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentCreateForm
    template_name = "create_b.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        context['action'] = 'Создание нового объекта'
        return context

class ComponentUpdateView(UpdateView):
    model = Component
    form_class = ComponentCreateForm
    template_name = "create_b.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        context['action'] = 'Редактирование объекта'
        return context

class ComponentDeleteView(DeleteView):
    model = Component
    success_url = '/component/list'
    template_name = "delete_b.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        return context

class ComponentDetailView(DetailView):    
    model = Component
    template_name = "detail_b.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        return context

class ComponentsListView(ListView):
    model = Component

    template_name = "list_com.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компонент'
        context['href'] = 'component'
        return context
