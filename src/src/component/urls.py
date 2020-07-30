from django.urls import path
from .models import Component

from .views import (ComponentListView,
                    ComponentCreateView,
                    ComponentUpdateView,
                    ComponentDeleteView,
                    ComponentDeleteView,
                    ComponentDetailView
                    ) 


component = [
    path ('list/', ComponentListView.as_view()),
    path ('create/', ComponentCreateView.as_view()),
    path ('update/<int:pk>/', ComponentUpdateView.as_view()),
    path ('delete/<int:pk>/', ComponentDeleteView.as_view()),
    path ('<int:pk>/', ComponentDetailView.as_view()),
]