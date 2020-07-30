from django.urls import path
from .models import Categorie, ManufacturingFirm

from .views import (CategorieListView,
                    CategorieCreateView,
                    CategorieUpdateView,
                    CategorieDeleteView,
                    CategorieDeleteView,
                    CategorieDetailView
                    )

from .views import (ManufacturingFirmListView,
                    ManufacturingFirmCreateView,
                    ManufacturingFirmUpdateView,
                    ManufacturingFirmDeleteView,
                    ManufacturingFirmDeleteView,
                    ManufacturingFirmDetailView
                    )

categorie = [
    path ('list/', CategorieListView.as_view()),
    path ('create/', CategorieCreateView.as_view()),
    path ('update/<int:pk>/', CategorieUpdateView.as_view()),
    path ('delete/<int:pk>/', CategorieDeleteView.as_view()),
    path ('<int:pk>/', CategorieDetailView.as_view()),
]


manufirm = [
    path ('list/', ManufacturingFirmListView.as_view()),
    path ('create/', ManufacturingFirmCreateView.as_view()),
    path ('update/<int:pk>/', ManufacturingFirmUpdateView.as_view()),
    path ('delete/<int:pk>/', ManufacturingFirmDeleteView.as_view()),
    path ('<int:pk>/', ManufacturingFirmDetailView.as_view()),
]

