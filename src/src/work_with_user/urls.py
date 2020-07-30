from django.urls import path
from .views import *

acaunt = [
    path('user/',  UserAkaunt.as_view(),name="user" ),
    path('logout/', LogOut.as_view(), name="logout"),
    path('change-password/',PasswordChange.as_view(), name="change-password"),
    path('register/', RegisterFormView.as_view(), name= 'register'),
]