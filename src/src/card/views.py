from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import ComponentInCard, Card
from component.models import Component
from .forms import ComponentInCardForm
from django.contrib.auth.models import User

# Create your views here.

class ComponentInCardUpdateView(UpdateView):
    model = ComponentInCard
    form_class = ComponentInCardForm
    template_name = "create_card.html"
    success_url = '/card/'
    def get_object(self):
        component_to_add = self.kwargs.get('pk')
        card_id = self.request.session.get('card_id')
        if not card_id:
            if self.request.user.is_anonymous:
                user = User.objects.get(pk=2)
            else:
                user = self.request.user
            card = Card.objects.create(user=user)
            self.request.session['card_id'] = card.pk
        else:
            card = Card.objects.get(pk=card_id)
        component = Component.objects.get(pk=component_to_add)
        component_in_card, created = ComponentInCard.objects.get_or_create(
            component=component,
            card=card,
            defaults={'price': component.price}
        )
        if not created:
            component_in_card.quantity = component_in_card.quantity + 1
            component_in_card.price = component.price * component_in_card.quantity
            component_in_card.save()
        return component_in_card

    def form_valid(self, form, **kwargs):
        quantity = form.cleaned_data.get('quantity')
        price = self.object.component.price
        total_price = quantity * price
        self.object.price = total_price
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ComponentInCardDeleteView(DeleteView):
    model = ComponentInCard
    success_url = '/card/'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ComponentInCardDetailView(DetailView):
    model = ComponentInCard
    template_name = "detail_card.html"

class CardListView(TemplateView):
    model = Card
    template_name = "list_card.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        card_id = self.request.session.get('card_id')
        card = None
        if card_id:
            card = Card.objects.get(pk=card_id)
        context['card'] = card
        context['title'] = 'Корзина для заказа'
        context['action'] = 'Пожалуйста, проверьте Ваш заказ'
        context['url'] = '/card'
        return context