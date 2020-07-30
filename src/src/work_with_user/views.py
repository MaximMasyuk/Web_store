from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
#Create your views here.


class PasswordChange (views.PasswordChangeView):

    template_name =  "registration/passwordChange.html"
    success_url = '/accounts/login/'

class LogOut (views.LogoutView):
    template_name =  "registration/logout.html"

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    
    template_name = "registration/register.html"

    def form_valid(self, form):
        
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class UserAkaunt(TemplateView):
    template_name = "registration/acaunt.html"