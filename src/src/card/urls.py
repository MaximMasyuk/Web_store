from django.urls import path
from .views import *

card = [
    path('add/<int:pk>/', ComponentInCardUpdateView.as_view(), name="add"),
    path('update/<int:pk>/', ComponentInCardUpdateView.as_view()),
    
   
]

componentincard = [
    path('delete/<int:pk>/', ComponentInCardDeleteView.as_view()),
    path('<int:pk>/', ComponentInCardDetailView.as_view()),
]