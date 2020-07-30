"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .import settings

from component_option.urls import categorie,manufirm
from component.urls import component
from work_with_user.urls import acaunt
from card.urls import card, componentincard

from component.views import ComponentsListView
from card.views import CardListView
from order.views import OrderUpdateView

admin = [
    path('admin/', admin.site.urls),
]

categorie = [
    path ('categorie/', include(categorie))
]

manufirm = [
    path('manufirm/',include (manufirm))
]

componnent = [
    path('component/', include(component)),
    path ('',ComponentsListView.as_view(), name= "home"),
]

acaunt = [
   path('accounts/', include('django.contrib.auth.urls')),
   path ("user/", include (acaunt))
]

cards =[
   path ('card/', CardListView.as_view(), name="list"), 
   path ('card/', include (card)),
   path ("componentincard/", include (componentincard))]


order = [
   path ('order/', OrderUpdateView.as_view(), ), 

]

urlpatterns = admin + categorie + manufirm + componnent + acaunt + cards + order + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)