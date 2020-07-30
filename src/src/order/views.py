from django.shortcuts import render
from django.views.generic.edit import UpdateView
from card.models import Card
from .models import Order
from .forms import OrderCreateForm

# Create your views here.

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "create_order.html"
    success_url = "/"
    def get_object(self):
        order_id = self.request.session.get('order_id')
        card_id = self.request.session.get('card_id')
        
        card = Card.objects.get(pk=card_id)
        # book = Book.objects.get(pk=book_to_add)
        order, created = Order.objects.get_or_create(
            card = card,
            price = card.total_price(),
            
        )
        if created:
            self.request.session["order_id"]= order.pk
        return order

    def get_success_url(self):
        order_id = self.request.session.get('order_id')
        card_id = self.request.session.get('card_id')

        order_id = None
        card_id = None
        return super().get_success_url()

   